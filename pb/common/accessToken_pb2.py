# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/accessToken.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/accessToken.proto',
  package='common',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x18\x63ommon/accessToken.proto\x12\x06\x63ommon\"\xb9\x02\n\x0b\x41\x63\x63\x65ssToken\x12\x0e\n\x06userId\x18\x01 \x01(\t\x12\x11\n\tcompanyId\x18\x02 \x01(\t\x12\x11\n\texpiresAt\x18\x03 \x01(\x03\x12\x39\n\x0bpermissions\x18\x04 \x03(\x0b\x32$.common.AccessToken.PermissionsEntry\x12\x0f\n\x07isGuest\x18\x06 \x01(\x08\x12\x13\n\x0b\x64isplayName\x18\x07 \x01(\t\x12\x19\n\x11\x62\x61sePermissionsId\x18\x08 \x01(\t\x12\x1b\n\x13\x65xtensionDisallowed\x18\n \x01(\x08\x1a\x32\n\x10PermissionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01J\x04\x08\x05\x10\x06J\x04\x08\t\x10\nR\x08metadataR\x11signingDisallowedb\x06proto3'
)




_ACCESSTOKEN_PERMISSIONSENTRY = _descriptor.Descriptor(
  name='PermissionsEntry',
  full_name='common.AccessToken.PermissionsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='common.AccessToken.PermissionsEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='common.AccessToken.PermissionsEntry.value', index=1,
      number=2, type=8, cpp_type=7, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=259,
  serialized_end=309,
)

_ACCESSTOKEN = _descriptor.Descriptor(
  name='AccessToken',
  full_name='common.AccessToken',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='userId', full_name='common.AccessToken.userId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='companyId', full_name='common.AccessToken.companyId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expiresAt', full_name='common.AccessToken.expiresAt', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='permissions', full_name='common.AccessToken.permissions', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isGuest', full_name='common.AccessToken.isGuest', index=4,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='displayName', full_name='common.AccessToken.displayName', index=5,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='basePermissionsId', full_name='common.AccessToken.basePermissionsId', index=6,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extensionDisallowed', full_name='common.AccessToken.extensionDisallowed', index=7,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ACCESSTOKEN_PERMISSIONSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=37,
  serialized_end=350,
)

_ACCESSTOKEN_PERMISSIONSENTRY.containing_type = _ACCESSTOKEN
_ACCESSTOKEN.fields_by_name['permissions'].message_type = _ACCESSTOKEN_PERMISSIONSENTRY
DESCRIPTOR.message_types_by_name['AccessToken'] = _ACCESSTOKEN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AccessToken = _reflection.GeneratedProtocolMessageType('AccessToken', (_message.Message,), {

  'PermissionsEntry' : _reflection.GeneratedProtocolMessageType('PermissionsEntry', (_message.Message,), {
    'DESCRIPTOR' : _ACCESSTOKEN_PERMISSIONSENTRY,
    '__module__' : 'common.accessToken_pb2'
    # @@protoc_insertion_point(class_scope:common.AccessToken.PermissionsEntry)
    })
  ,
  'DESCRIPTOR' : _ACCESSTOKEN,
  '__module__' : 'common.accessToken_pb2'
  # @@protoc_insertion_point(class_scope:common.AccessToken)
  })
_sym_db.RegisterMessage(AccessToken)
_sym_db.RegisterMessage(AccessToken.PermissionsEntry)


_ACCESSTOKEN_PERMISSIONSENTRY._options = None
# @@protoc_insertion_point(module_scope)
