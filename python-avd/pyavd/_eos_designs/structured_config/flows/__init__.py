# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from ...._errors import AristaAvdMissingVariableError
from ...._utils import get, get_item, strip_null_from_data
from ....j2filters import natural_sort
from ...avdfacts import AvdFacts


class AvdStructuredConfigFlows(AvdFacts):
    """
    This class must be rendered after all other eos_designs modules since it relies on
    detecting sflow from the interface structured config generated by the other modules.

    The only exception is of course custom_structured_configuration which always comes last.
    """

    @cached_property
    def sflow(self) -> dict | None:
        """
        Structured config for sFlow.

        Only configure if any interface is enabled for sFlow.

        Covers:
        - sflow_settings
        - source-interfaces based on source_interfaces.sflow
        """
        if not self._enable_sflow:
            return None

        destinations = get(self._hostvars, "sflow_settings.destinations")
        if destinations is None:
            # TODO:
            # AVD5.0.0 raise an error if sflow is enabled on an interface but there are no destinations configured.
            # This cannot be implemented today since it would be breaking for already released support for sflow on interfaces.
            return None

        sflow_settings_vrfs = get(self._hostvars, "sflow_settings.vrfs", default=[])

        # At this point we have at least one interface with sFlow enabled
        # and at least one destination.
        sflow = {
            "run": True,
            "sample": get(self._hostvars, "sflow_settings.sample.rate"),
        }

        # Using a temporary dict for VRFs
        sflow_vrfs = {}

        for destination in natural_sort(destinations, "destination"):
            vrf = get(destination, "vrf")
            if vrf is None:
                vrf = self.shared_utils.default_mgmt_protocol_vrf
                source_interface = self.shared_utils.default_mgmt_protocol_interface

            elif vrf == "use_mgmt_interface_vrf":
                if (self.shared_utils.mgmt_ip is None) and (self.shared_utils.ipv6_mgmt_ip is None):
                    raise AristaAvdMissingVariableError(
                        "Unable to configure sFlow source-interface with 'use_mgmt_interface_vrf' since 'mgmt_ip' or 'ipv6_mgmt_ip' are not set."
                    )

                vrf = self.shared_utils.mgmt_interface_vrf
                source_interface = get(get_item(sflow_settings_vrfs, "name", vrf, default={}), "source_interface", default=self.shared_utils.mgmt_interface)

            elif vrf == "use_inband_mgmt_vrf":
                # Check for missing interface
                if self.shared_utils.inband_mgmt_interface is None:
                    raise AristaAvdMissingVariableError(
                        "Unable to configure sFlow source-interface with 'use_inband_mgmt_vrf' since 'inband_mgmt_interface' is not set."
                    )

                # self.shared_utils.inband_mgmt_vrf returns None for the default VRF, but here we need "default" to avoid duplicates.
                vrf = self.shared_utils.inband_mgmt_vrf or "default"
                source_interface = get(
                    get_item(sflow_settings_vrfs, "name", vrf, default={}), "source_interface", default=self.shared_utils.inband_mgmt_interface
                )

            else:
                # Default is none, meaning we will not configure a source interface for this VRF.
                source_interface = get(get_item(sflow_settings_vrfs, "name", vrf, default={}), "source_interface")

            if vrf in [None, "default"]:
                # Add destination without VRF field
                sflow.setdefault("destinations", []).append(
                    {
                        "destination": destination.get("destination"),
                        "port": destination.get("port"),
                    }
                )
                sflow["source_interface"] = source_interface

            else:
                # Add destination with VRF field.
                sflow_vrfs.setdefault(vrf, {}).setdefault("destinations", []).append(
                    {
                        "destination": destination.get("destination"),
                        "port": destination.get("port"),
                    }
                )
                sflow_vrfs[vrf]["source_interface"] = source_interface

        # convert sflow_vrfs dict into list and insert into sflow
        if sflow_vrfs:
            sflow["vrfs"] = [{"name": vrf_name, **vrf} for vrf_name, vrf in sflow_vrfs.items()]

        return strip_null_from_data(sflow)

    @cached_property
    def _enable_sflow(self) -> bool:
        """
        Enable sFlow if any interface is enabled for sFlow.

        This relies on sFlow being rendered after all other eos_designs modules (except structured config).
        """
        for interface in get(self._hostvars, "ethernet_interfaces", default=[]):
            if get(interface, "sflow.enable") is True:
                return True

        for interface in get(self._hostvars, "port_channel_interfaces", default=[]):
            if get(interface, "sflow.enable") is True:
                return True

        return False

    @cached_property
    def _default_flow_tracker(self) -> dict:
        """
        Following configuration will be rendered based on the inputs:
        tracker FLOW-TRACKER
            record export on inactive timeout 70000
            record export on interval 300000
            exporter ayush_exporter
                collector 127.0.0.1
                local interface Loopback0
                template interval 3600000

        Depending on the flow tracker type, some other default values like sample, no shutdown
        will be added in further method
        """
        return {
            "name": self.shared_utils.default_flow_tracker_name,
            "record_export": {"on_inactive_timeout": 70000, "on_interval": 300000},
            "exporters": [{"name": "CV-TELEMETRY", "collector": {"host": "127.0.0.1"}, "local_interface": "Loopback0", "template_interval": 3600000}],
        }

    def resolve_flow_tracker_by_type(self, tracker_settings: dict) -> dict:
        tracker = {
            "name": tracker_settings["name"],
            "record_export": tracker_settings.get("record_export"),
            "exporters": tracker_settings.get("exporters"),
        }
        if self.shared_utils.flow_tracking_type == "sampled":
            sampled_settings = get(tracker_settings, "sampled", {})
            if (table_size := sampled_settings.get("table_size")) is not None:
                tracker["table_size"] = table_size
            if (mpls := get(sampled_settings, "record_export.mpls")) is not None:
                tracker["record_export"]["mpls"] = mpls

        return tracker

    @cached_property
    def flow_tracking(self) -> dict | None:
        """
        Return structured config for flow_tracking
        """
        configured_trackers = self._get_enabled_flow_trackers()
        if not configured_trackers:
            return None

        flow_tracking = {}

        tracker_type = self.shared_utils.flow_tracking_type
        flow_tracking_settings = get(self._hostvars, "flow_tracking_settings", default={})
        global_settings = get(flow_tracking_settings, tracker_type, default={})
        flow_tracking[tracker_type] = global_settings.copy()
        if tracker_type == "sampled":
            flow_tracking[tracker_type]["sample"] = get(flow_tracking[tracker_type], "sample", 10000)

        all_trackers = get(flow_tracking_settings, "trackers", default=[])

        filtered_trackers = []
        for tracker_name in configured_trackers:
            """
            We allow overriding the default flow tracker name, so if user has configured a tracker
            with the default tracker name, then we just use that, if not, we create a default config
            """
            default_tracker = tracker_name == self.shared_utils.default_flow_tracker_name
            tracker = get_item(
                all_trackers,
                "name",
                tracker_name,
                required=not default_tracker,
                custom_error_msg=f"{tracker_name} is being used for one of the interfaces, but is not configured in flow_tracking_settings",
            )
            if default_tracker and tracker is None:
                tracker = self._default_flow_tracker

            filtered_trackers.append(self.resolve_flow_tracker_by_type(tracker))

        flow_tracking[tracker_type]["trackers"] = filtered_trackers
        flow_tracking[tracker_type]["shutdown"] = False

        return flow_tracking

    def _get_enabled_flow_trackers(self) -> bool:
        """
        Enable flow-tracking if any interface is enabled for flow-tracking.

        This relies on flow-tracking being rendered after all other eos_designs modules (except structured config).
        """
        trackers = {
            "sampled": {},
            "hardware": {},
        }

        for interface_type in ["ethernet_interfaces", "port_channel_interfaces", "dps_interfaces"]:
            for interface in get(self._hostvars, interface_type, default=[]):
                if tracker := get(interface, "flow_tracker"):
                    for trackerType, trackerName in tracker.items():
                        trackers[trackerType][trackerName] = True

        return trackers[self.shared_utils.flow_tracking_type]
