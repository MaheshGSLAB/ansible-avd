=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ip_radius_source_interfaces</samp>](## "ip_radius_source_interfaces") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "ip_radius_source_interfaces.[].name") | String |  |  |  | Interface Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "ip_radius_source_interfaces.[].vrf") | String |  |  |  | VRF Name |

=== "YAML"

    ```yaml
    ip_radius_source_interfaces:
      - name: <str>
        vrf: <str>
    ```