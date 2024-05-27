# Copyright (c) 2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: fmp/deletes.proto, fmp/extensions.proto, fmp/inet.proto, fmp/pages.proto, fmp/wrappers.proto, fmp/yang.proto
# plugin: python-aristaproto
# This file has been @generated

from dataclasses import dataclass
from typing import (
    Dict,
    List,
)

try:
    import aristaproto
except ImportError:
    HAS_ARISTAPROTO = False
    from ansible_collections.arista.avd.plugins.plugin_utils.cv_client.mocked_classes import mocked_aristaproto as aristaproto
else:
    HAS_ARISTAPROTO = True


class SortDirection(aristaproto.Enum):
    """
    SortDirection is an enum of possible values for direction of sorting.
    """

    UNSPECIFIED = 0
    """SORT_DIRECTION_UNSPECIFIED means that no sort direction specified."""

    ASCENDING = 1
    """SORT_DIRECTION_ASCENDING sorts in ascending order."""

    DESCENDING = 2
    """SORT_DIRECTION_DESCENDING sorts in descending order."""


class DeleteError(aristaproto.Enum):
    """DeleteError defines the set of delete error types."""

    UNSPECIFIED = 0
    """
    DELETE_ERROR_UNSPECIFIED indicates that the delete error
     is not specified.
    """

    UNAUTHORIZED = 1
    """
    DELETE_ERROR_UNAUTHORIZED indicates that the user is not authorized
     to perform the specified delete.
    """

    INTERNAL = 2
    """
    DELETE_ERROR_INTERNAL indicates that the server encountered an
     unrecoverable error on the specified delete.
    """

    UNDELETABLE_KEY = 3
    """
    DELETE_ERROR_UNDELETABLE_KEY indicates that the specified error is
     not allowed by the service.
    """


@dataclass(eq=False, repr=False)
class MacAddress(aristaproto.Message):
    value: str = aristaproto.string_field(1)


@dataclass(eq=False, repr=False)
class RepeatedMacAddress(aristaproto.Message):
    values: List["MacAddress"] = aristaproto.message_field(1)


@dataclass(eq=False, repr=False)
class IpAddress(aristaproto.Message):
    value: str = aristaproto.string_field(1)


@dataclass(eq=False, repr=False)
class RepeatedIpAddress(aristaproto.Message):
    values: List["IpAddress"] = aristaproto.message_field(1)


@dataclass(eq=False, repr=False)
class IPv4Address(aristaproto.Message):
    value: str = aristaproto.string_field(1)


@dataclass(eq=False, repr=False)
class RepeatedIPv4Address(aristaproto.Message):
    values: List["IPv4Address"] = aristaproto.message_field(1)


@dataclass(eq=False, repr=False)
class IPv6Address(aristaproto.Message):
    value: str = aristaproto.string_field(1)


@dataclass(eq=False, repr=False)
class RepeatedIPv6Address(aristaproto.Message):
    values: List["IPv6Address"] = aristaproto.message_field(1)


@dataclass(eq=False, repr=False)
class IpPrefix(aristaproto.Message):
    value: str = aristaproto.string_field(1)


@dataclass(eq=False, repr=False)
class IPv4Prefix(aristaproto.Message):
    value: str = aristaproto.string_field(1)


@dataclass(eq=False, repr=False)
class IPv6Prefix(aristaproto.Message):
    value: str = aristaproto.string_field(1)


@dataclass(eq=False, repr=False)
class Port(aristaproto.Message):
    value: int = aristaproto.uint32_field(1)


@dataclass(eq=False, repr=False)
class RepeatedDouble(aristaproto.Message):
    """Wrapper message for `repeated double`."""

    values: List[float] = aristaproto.double_field(1)
    """The repeated double values."""


@dataclass(eq=False, repr=False)
class RepeatedFloat(aristaproto.Message):
    """Wrapper message for `repeated float`."""

    values: List[float] = aristaproto.float_field(1)
    """The repeated float values."""


@dataclass(eq=False, repr=False)
class RepeatedInt64(aristaproto.Message):
    """Wrapper message for `repeated int64`."""

    values: List[int] = aristaproto.int64_field(1)
    """The repeated int64 values."""


@dataclass(eq=False, repr=False)
class RepeatedUInt64(aristaproto.Message):
    """Wrapper message for `repeated uint64`."""

    values: List[int] = aristaproto.uint64_field(1)
    """The repeated uint64 values."""


@dataclass(eq=False, repr=False)
class RepeatedInt32(aristaproto.Message):
    """Wrapper message for `repeated int32`."""

    values: List[int] = aristaproto.int32_field(1)
    """The repeated int32 values."""


@dataclass(eq=False, repr=False)
class RepeatedUInt32(aristaproto.Message):
    """Wrapper message for `repeated uint32`."""

    values: List[int] = aristaproto.uint32_field(1)
    """The repeated uint32 values."""


@dataclass(eq=False, repr=False)
class RepeatedBool(aristaproto.Message):
    """Wrapper message for `repeated bool`."""

    values: List[bool] = aristaproto.bool_field(1)
    """The repeated bool values."""


@dataclass(eq=False, repr=False)
class RepeatedString(aristaproto.Message):
    """Wrapper message for `repeated string`."""

    values: List[str] = aristaproto.string_field(1)
    """The repeated string values."""


@dataclass(eq=False, repr=False)
class RepeatedBytes(aristaproto.Message):
    """Wrapper message for `repeated bytes`."""

    values: List[bytes] = aristaproto.bytes_field(1)
    """The repeated bytes values."""


@dataclass(eq=False, repr=False)
class MapInt64Double(aristaproto.Message):
    """Wrapper message for `map<int64, double>`."""

    values: Dict[int, float] = aristaproto.map_field(
        1, aristaproto.TYPE_INT64, aristaproto.TYPE_DOUBLE
    )
    """The map<int64, double> values."""


@dataclass(eq=False, repr=False)
class MapInt64Float(aristaproto.Message):
    """Wrapper message for `map<int64, float>`."""

    values: Dict[int, float] = aristaproto.map_field(
        1, aristaproto.TYPE_INT64, aristaproto.TYPE_FLOAT
    )
    """The map<int64, float> values."""


@dataclass(eq=False, repr=False)
class MapInt64Int64(aristaproto.Message):
    """Wrapper message for `map<int64, int64>`."""

    values: Dict[int, int] = aristaproto.map_field(
        1, aristaproto.TYPE_INT64, aristaproto.TYPE_INT64
    )
    """The map<int64, int64> values."""


@dataclass(eq=False, repr=False)
class MapInt64UInt64(aristaproto.Message):
    """Wrapper message for `map<int64, uint64>`."""

    values: Dict[int, int] = aristaproto.map_field(
        1, aristaproto.TYPE_INT64, aristaproto.TYPE_UINT64
    )
    """The map<int64, uint64> values."""


@dataclass(eq=False, repr=False)
class MapInt64Int32(aristaproto.Message):
    """Wrapper message for `map<int64, int32>`."""

    values: Dict[int, int] = aristaproto.map_field(
        1, aristaproto.TYPE_INT64, aristaproto.TYPE_INT32
    )
    """The map<int64, int32> values."""


@dataclass(eq=False, repr=False)
class MapInt64UInt32(aristaproto.Message):
    """Wrapper message for `map<int64, uint32>`."""

    values: Dict[int, int] = aristaproto.map_field(
        1, aristaproto.TYPE_INT64, aristaproto.TYPE_UINT32
    )
    """The map<int64, uint32> values."""


@dataclass(eq=False, repr=False)
class MapInt64Bool(aristaproto.Message):
    """Wrapper message for `map<int64, bool>`."""

    values: Dict[int, bool] = aristaproto.map_field(
        1, aristaproto.TYPE_INT64, aristaproto.TYPE_BOOL
    )
    """The map<int64, bool> values."""


@dataclass(eq=False, repr=False)
class MapInt64String(aristaproto.Message):
    """Wrapper message for `map<int64, string>`."""

    values: Dict[int, str] = aristaproto.map_field(
        1, aristaproto.TYPE_INT64, aristaproto.TYPE_STRING
    )
    """The map<int64, string> values."""


@dataclass(eq=False, repr=False)
class MapInt64Bytes(aristaproto.Message):
    """Wrapper message for `map<int64, bytes>`."""

    values: Dict[int, bytes] = aristaproto.map_field(
        1, aristaproto.TYPE_INT64, aristaproto.TYPE_BYTES
    )
    """The map<int64, bytes> values."""


@dataclass(eq=False, repr=False)
class MapUInt64Double(aristaproto.Message):
    """Wrapper message for `map<uint64, double>`."""

    values: Dict[int, float] = aristaproto.map_field(
        1, aristaproto.TYPE_UINT64, aristaproto.TYPE_DOUBLE
    )
    """The map<uint64, double> values."""


@dataclass(eq=False, repr=False)
class MapUInt64Float(aristaproto.Message):
    """Wrapper message for `map<uint64, float>`."""

    values: Dict[int, float] = aristaproto.map_field(
        1, aristaproto.TYPE_UINT64, aristaproto.TYPE_FLOAT
    )
    """The map<uint64, float> values."""


@dataclass(eq=False, repr=False)
class MapUInt64Int64(aristaproto.Message):
    """Wrapper message for `map<uint64, int64>`."""

    values: Dict[int, int] = aristaproto.map_field(
        1, aristaproto.TYPE_UINT64, aristaproto.TYPE_INT64
    )
    """The map<uint64, int64> values."""


@dataclass(eq=False, repr=False)
class MapUInt64UInt64(aristaproto.Message):
    """Wrapper message for `map<uint64, uint64>`."""

    values: Dict[int, int] = aristaproto.map_field(
        1, aristaproto.TYPE_UINT64, aristaproto.TYPE_UINT64
    )
    """The map<uint64, uint64> values."""


@dataclass(eq=False, repr=False)
class MapUInt64Int32(aristaproto.Message):
    """Wrapper message for `map<uint64, int32>`."""

    values: Dict[int, int] = aristaproto.map_field(
        1, aristaproto.TYPE_UINT64, aristaproto.TYPE_INT32
    )
    """The map<uint64, int32> values."""


@dataclass(eq=False, repr=False)
class MapUInt64UInt32(aristaproto.Message):
    """Wrapper message for `map<uint64, uint32>`."""

    values: Dict[int, int] = aristaproto.map_field(
        1, aristaproto.TYPE_UINT64, aristaproto.TYPE_UINT32
    )
    """The map<uint64, uint32> values."""


@dataclass(eq=False, repr=False)
class MapUInt64Bool(aristaproto.Message):
    """Wrapper message for `map<uint64, bool>`."""

    values: Dict[int, bool] = aristaproto.map_field(
        1, aristaproto.TYPE_UINT64, aristaproto.TYPE_BOOL
    )
    """The map<uint64, bool> values."""


@dataclass(eq=False, repr=False)
class MapUInt64String(aristaproto.Message):
    """Wrapper message for `map<uint64, string>`."""

    values: Dict[int, str] = aristaproto.map_field(
        1, aristaproto.TYPE_UINT64, aristaproto.TYPE_STRING
    )
    """The map<uint64, string> values."""


@dataclass(eq=False, repr=False)
class MapUInt64Bytes(aristaproto.Message):
    """Wrapper message for `map<uint64, bytes>`."""

    values: Dict[int, bytes] = aristaproto.map_field(
        1, aristaproto.TYPE_UINT64, aristaproto.TYPE_BYTES
    )
    """The map<uint64, bytes> values."""


@dataclass(eq=False, repr=False)
class MapInt32Double(aristaproto.Message):
    """Wrapper message for `map<int32, double>`."""

    values: Dict[int, float] = aristaproto.map_field(
        1, aristaproto.TYPE_INT32, aristaproto.TYPE_DOUBLE
    )
    """The map<int32, double> values."""


@dataclass(eq=False, repr=False)
class MapInt32Float(aristaproto.Message):
    """Wrapper message for `map<int32, float>`."""

    values: Dict[int, float] = aristaproto.map_field(
        1, aristaproto.TYPE_INT32, aristaproto.TYPE_FLOAT
    )
    """The map<int32, float> values."""


@dataclass(eq=False, repr=False)
class MapInt32Int64(aristaproto.Message):
    """Wrapper message for `map<int32, int64>`."""

    values: Dict[int, int] = aristaproto.map_field(
        1, aristaproto.TYPE_INT32, aristaproto.TYPE_INT64
    )
    """The map<int32, int64> values."""


@dataclass(eq=False, repr=False)
class MapInt32UInt64(aristaproto.Message):
    """Wrapper message for `map<int32, uint64>`."""

    values: Dict[int, int] = aristaproto.map_field(
        1, aristaproto.TYPE_INT32, aristaproto.TYPE_UINT64
    )
    """The map<int32, uint64> values."""


@dataclass(eq=False, repr=False)
class MapInt32Int32(aristaproto.Message):
    """Wrapper message for `map<int32, int32>`."""

    values: Dict[int, int] = aristaproto.map_field(
        1, aristaproto.TYPE_INT32, aristaproto.TYPE_INT32
    )
    """The map<int32, int32> values."""


@dataclass(eq=False, repr=False)
class MapInt32UInt32(aristaproto.Message):
    """Wrapper message for `map<int32, uint32>`."""

    values: Dict[int, int] = aristaproto.map_field(
        1, aristaproto.TYPE_INT32, aristaproto.TYPE_UINT32
    )
    """The map<int32, uint32> values."""


@dataclass(eq=False, repr=False)
class MapInt32Bool(aristaproto.Message):
    """Wrapper message for `map<int32, bool>`."""

    values: Dict[int, bool] = aristaproto.map_field(
        1, aristaproto.TYPE_INT32, aristaproto.TYPE_BOOL
    )
    """The map<int32, bool> values."""


@dataclass(eq=False, repr=False)
class MapInt32String(aristaproto.Message):
    """Wrapper message for `map<int32, string>`."""

    values: Dict[int, str] = aristaproto.map_field(
        1, aristaproto.TYPE_INT32, aristaproto.TYPE_STRING
    )
    """The map<int32, string> values."""


@dataclass(eq=False, repr=False)
class MapInt32Bytes(aristaproto.Message):
    """Wrapper message for `map<int32, bytes>`."""

    values: Dict[int, bytes] = aristaproto.map_field(
        1, aristaproto.TYPE_INT32, aristaproto.TYPE_BYTES
    )
    """The map<int32, bytes> values."""


@dataclass(eq=False, repr=False)
class MapUInt32Double(aristaproto.Message):
    """Wrapper message for `map<uint32, double>`."""

    values: Dict[int, float] = aristaproto.map_field(
        1, aristaproto.TYPE_UINT32, aristaproto.TYPE_DOUBLE
    )
    """The map<uint32, double> values."""


@dataclass(eq=False, repr=False)
class MapUInt32Float(aristaproto.Message):
    """Wrapper message for `map<uint32, float>`."""

    values: Dict[int, float] = aristaproto.map_field(
        1, aristaproto.TYPE_UINT32, aristaproto.TYPE_FLOAT
    )
    """The map<uint32, float> values."""


@dataclass(eq=False, repr=False)
class MapUInt32Int64(aristaproto.Message):
    """Wrapper message for `map<uint32, int64>`."""

    values: Dict[int, int] = aristaproto.map_field(
        1, aristaproto.TYPE_UINT32, aristaproto.TYPE_INT64
    )
    """The map<uint32, int64> values."""


@dataclass(eq=False, repr=False)
class MapUInt32UInt64(aristaproto.Message):
    """Wrapper message for `map<uint32, uint64>`."""

    values: Dict[int, int] = aristaproto.map_field(
        1, aristaproto.TYPE_UINT32, aristaproto.TYPE_UINT64
    )
    """The map<uint32, uint64> values."""


@dataclass(eq=False, repr=False)
class MapUInt32Int32(aristaproto.Message):
    """Wrapper message for `map<uint32, int32>`."""

    values: Dict[int, int] = aristaproto.map_field(
        1, aristaproto.TYPE_UINT32, aristaproto.TYPE_INT32
    )
    """The map<uint32, int32> values."""


@dataclass(eq=False, repr=False)
class MapUInt32UInt32(aristaproto.Message):
    """Wrapper message for `map<uint32, uint32>`."""

    values: Dict[int, int] = aristaproto.map_field(
        1, aristaproto.TYPE_UINT32, aristaproto.TYPE_UINT32
    )
    """The map<uint32, uint32> values."""


@dataclass(eq=False, repr=False)
class MapUInt32Bool(aristaproto.Message):
    """Wrapper message for `map<uint32, bool>`."""

    values: Dict[int, bool] = aristaproto.map_field(
        1, aristaproto.TYPE_UINT32, aristaproto.TYPE_BOOL
    )
    """The map<uint32, bool> values."""


@dataclass(eq=False, repr=False)
class MapUInt32String(aristaproto.Message):
    """Wrapper message for `map<uint32, string>`."""

    values: Dict[int, str] = aristaproto.map_field(
        1, aristaproto.TYPE_UINT32, aristaproto.TYPE_STRING
    )
    """The map<uint32, string> values."""


@dataclass(eq=False, repr=False)
class MapUInt32Bytes(aristaproto.Message):
    """Wrapper message for `map<uint32, bytes>`."""

    values: Dict[int, bytes] = aristaproto.map_field(
        1, aristaproto.TYPE_UINT32, aristaproto.TYPE_BYTES
    )
    """The map<uint32, bytes> values."""


@dataclass(eq=False, repr=False)
class MapBoolDouble(aristaproto.Message):
    """Wrapper message for `map<bool, double>`."""

    values: Dict[bool, float] = aristaproto.map_field(
        1, aristaproto.TYPE_BOOL, aristaproto.TYPE_DOUBLE
    )
    """The map<bool, double> values."""


@dataclass(eq=False, repr=False)
class MapBoolFloat(aristaproto.Message):
    """Wrapper message for `map<bool, float>`."""

    values: Dict[bool, float] = aristaproto.map_field(
        1, aristaproto.TYPE_BOOL, aristaproto.TYPE_FLOAT
    )
    """The map<bool, float> values."""


@dataclass(eq=False, repr=False)
class MapBoolInt64(aristaproto.Message):
    """Wrapper message for `map<bool, int64>`."""

    values: Dict[bool, int] = aristaproto.map_field(
        1, aristaproto.TYPE_BOOL, aristaproto.TYPE_INT64
    )
    """The map<bool, int64> values."""


@dataclass(eq=False, repr=False)
class MapBoolUInt64(aristaproto.Message):
    """Wrapper message for `map<bool, uint64>`."""

    values: Dict[bool, int] = aristaproto.map_field(
        1, aristaproto.TYPE_BOOL, aristaproto.TYPE_UINT64
    )
    """The map<bool, uint64> values."""


@dataclass(eq=False, repr=False)
class MapBoolInt32(aristaproto.Message):
    """Wrapper message for `map<bool, int32>`."""

    values: Dict[bool, int] = aristaproto.map_field(
        1, aristaproto.TYPE_BOOL, aristaproto.TYPE_INT32
    )
    """The map<bool, int32> values."""


@dataclass(eq=False, repr=False)
class MapBoolUInt32(aristaproto.Message):
    """Wrapper message for `map<bool, uint32>`."""

    values: Dict[bool, int] = aristaproto.map_field(
        1, aristaproto.TYPE_BOOL, aristaproto.TYPE_UINT32
    )
    """The map<bool, uint32> values."""


@dataclass(eq=False, repr=False)
class MapBoolBool(aristaproto.Message):
    """Wrapper message for `map<bool, bool>`."""

    values: Dict[bool, bool] = aristaproto.map_field(
        1, aristaproto.TYPE_BOOL, aristaproto.TYPE_BOOL
    )
    """The map<bool, bool> values."""


@dataclass(eq=False, repr=False)
class MapBoolString(aristaproto.Message):
    """Wrapper message for `map<bool, string>`."""

    values: Dict[bool, str] = aristaproto.map_field(
        1, aristaproto.TYPE_BOOL, aristaproto.TYPE_STRING
    )
    """The map<bool, string> values."""


@dataclass(eq=False, repr=False)
class MapBoolBytes(aristaproto.Message):
    """Wrapper message for `map<bool, bytes>`."""

    values: Dict[bool, bytes] = aristaproto.map_field(
        1, aristaproto.TYPE_BOOL, aristaproto.TYPE_BYTES
    )
    """The map<bool, bytes> values."""


@dataclass(eq=False, repr=False)
class MapStringDouble(aristaproto.Message):
    """Wrapper message for `map<string, double>`."""

    values: Dict[str, float] = aristaproto.map_field(
        1, aristaproto.TYPE_STRING, aristaproto.TYPE_DOUBLE
    )
    """The map<string, double> values."""


@dataclass(eq=False, repr=False)
class MapStringFloat(aristaproto.Message):
    """Wrapper message for `map<string, float>`."""

    values: Dict[str, float] = aristaproto.map_field(
        1, aristaproto.TYPE_STRING, aristaproto.TYPE_FLOAT
    )
    """The map<string, float> values."""


@dataclass(eq=False, repr=False)
class MapStringInt64(aristaproto.Message):
    """Wrapper message for `map<string, int64>`."""

    values: Dict[str, int] = aristaproto.map_field(
        1, aristaproto.TYPE_STRING, aristaproto.TYPE_INT64
    )
    """The map<string, int64> values."""


@dataclass(eq=False, repr=False)
class MapStringUInt64(aristaproto.Message):
    """Wrapper message for `map<string, uint64>`."""

    values: Dict[str, int] = aristaproto.map_field(
        1, aristaproto.TYPE_STRING, aristaproto.TYPE_UINT64
    )
    """The map<string, uint64> values."""


@dataclass(eq=False, repr=False)
class MapStringInt32(aristaproto.Message):
    """Wrapper message for `map<string, int32>`."""

    values: Dict[str, int] = aristaproto.map_field(
        1, aristaproto.TYPE_STRING, aristaproto.TYPE_INT32
    )
    """The map<string, int32> values."""


@dataclass(eq=False, repr=False)
class MapStringUInt32(aristaproto.Message):
    """Wrapper message for `map<string, uint32>`."""

    values: Dict[str, int] = aristaproto.map_field(
        1, aristaproto.TYPE_STRING, aristaproto.TYPE_UINT32
    )
    """The map<string, uint32> values."""


@dataclass(eq=False, repr=False)
class MapStringBool(aristaproto.Message):
    """Wrapper message for `map<string, bool>`."""

    values: Dict[str, bool] = aristaproto.map_field(
        1, aristaproto.TYPE_STRING, aristaproto.TYPE_BOOL
    )
    """The map<string, bool> values."""


@dataclass(eq=False, repr=False)
class MapStringString(aristaproto.Message):
    """Wrapper message for `map<string, string>`."""

    values: Dict[str, str] = aristaproto.map_field(
        1, aristaproto.TYPE_STRING, aristaproto.TYPE_STRING
    )
    """The map<string, string> values."""


@dataclass(eq=False, repr=False)
class MapStringBytes(aristaproto.Message):
    """Wrapper message for `map<string, bytes>`."""

    values: Dict[str, bytes] = aristaproto.map_field(
        1, aristaproto.TYPE_STRING, aristaproto.TYPE_BYTES
    )
    """The map<string, bytes> values."""
