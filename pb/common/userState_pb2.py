# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/userState.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/userState.proto',
  package='common',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x16\x63ommon/userState.proto\x12\x06\x63ommon*\x99\x01\n\tUserState\x12\r\n\tCONNECTED\x10\x00\x12\r\n\tTIMED_OUT\x10\x01\x12\r\n\tLEFT_ROOM\x10\x02\x12\x08\n\x04QUIT\x10\x03\x12\n\n\x06KICKED\x10\x04\x12\x0e\n\nUSER_ERROR\x10\x05\x12\x0c\n\x08UPDATING\x10\x06\x12\x10\n\x0cSYSTEM_ERROR\x10\x07\x12\x0b\n\x07\x43REATED\x10\x08\x12\x0c\n\x08ON_BREAK\x10\tb\x06proto3'
)

_USERSTATE = _descriptor.EnumDescriptor(
  name='UserState',
  full_name='common.UserState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CONNECTED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIMED_OUT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEFT_ROOM', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUIT', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KICKED', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USER_ERROR', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATING', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYSTEM_ERROR', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CREATED', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ON_BREAK', index=9, number=9,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=35,
  serialized_end=188,
)
_sym_db.RegisterEnumDescriptor(_USERSTATE)

UserState = enum_type_wrapper.EnumTypeWrapper(_USERSTATE)
CONNECTED = 0
TIMED_OUT = 1
LEFT_ROOM = 2
QUIT = 3
KICKED = 4
USER_ERROR = 5
UPDATING = 6
SYSTEM_ERROR = 7
CREATED = 8
ON_BREAK = 9


DESCRIPTOR.enum_types_by_name['UserState'] = _USERSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
