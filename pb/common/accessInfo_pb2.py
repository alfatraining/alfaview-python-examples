# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/accessInfo.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/accessInfo.proto',
  package='common',
  syntax='proto3',
  serialized_options=b'\370\001\001',
  serialized_pb=b'\n\x17\x63ommon/accessInfo.proto\x12\x06\x63ommon\"j\n\nAccessInfo\x12\x11\n\trequestId\x18\x01 \x01(\t\x12\x13\n\x0b\x61\x63\x63\x65ssToken\x18\x02 \x01(\x0c\x12\x17\n\x0fincludeMetadata\x18\x03 \x01(\x08\x12\x1b\n\x13returnObjectIdsOnly\x18\x04 \x01(\x08\x42\x03\xf8\x01\x01\x62\x06proto3'
)




_ACCESSINFO = _descriptor.Descriptor(
  name='AccessInfo',
  full_name='common.AccessInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='requestId', full_name='common.AccessInfo.requestId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='accessToken', full_name='common.AccessInfo.accessToken', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='includeMetadata', full_name='common.AccessInfo.includeMetadata', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='returnObjectIdsOnly', full_name='common.AccessInfo.returnObjectIdsOnly', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=35,
  serialized_end=141,
)

DESCRIPTOR.message_types_by_name['AccessInfo'] = _ACCESSINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AccessInfo = _reflection.GeneratedProtocolMessageType('AccessInfo', (_message.Message,), {
  'DESCRIPTOR' : _ACCESSINFO,
  '__module__' : 'common.accessInfo_pb2'
  # @@protoc_insertion_point(class_scope:common.AccessInfo)
  })
_sym_db.RegisterMessage(AccessInfo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
