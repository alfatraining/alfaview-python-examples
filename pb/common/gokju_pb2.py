# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/gokju.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/gokju.proto',
  package='common',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x12\x63ommon/gokju.proto\x12\x06\x63ommon\"\x1e\n\x0cTrackingInfo\x12\x0e\n\x06taskId\x18\x01 \x01(\tb\x06proto3'
)




_TRACKINGINFO = _descriptor.Descriptor(
  name='TrackingInfo',
  full_name='common.TrackingInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='taskId', full_name='common.TrackingInfo.taskId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=60,
)

DESCRIPTOR.message_types_by_name['TrackingInfo'] = _TRACKINGINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TrackingInfo = _reflection.GeneratedProtocolMessageType('TrackingInfo', (_message.Message,), {
  'DESCRIPTOR' : _TRACKINGINFO,
  '__module__' : 'common.gokju_pb2'
  # @@protoc_insertion_point(class_scope:common.TrackingInfo)
  })
_sym_db.RegisterMessage(TrackingInfo)


# @@protoc_insertion_point(module_scope)