# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/room.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pb.common import permissions_pb2 as common_dot_permissions__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/room.proto',
  package='common',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x11\x63ommon/room.proto\x12\x06\x63ommon\x1a\x18\x63ommon/permissions.proto\"\xed\x04\n\x04Room\x12\x13\n\x0b\x64isplayName\x18\x03 \x01(\t\x12\x1e\n\x04mode\x18\x04 \x01(\x0e\x32\x10.common.RoomMode\x12\"\n\x06quotas\x18\x06 \x01(\x0b\x32\x12.common.RoomQuotas\x12\x1e\n\x04type\x18\t \x01(\x0e\x32\x10.common.RoomType\x12,\n\x08metadata\x18\n \x03(\x0b\x32\x1a.common.Room.MetadataEntry\x12\x32\n\x0bpermissions\x18\x14 \x03(\x0b\x32\x1d.common.Room.PermissionsEntry\x12/\n\x12\x64\x65\x66\x61ultPermissions\x18\x15 \x01(\x0b\x32\x13.common.Permissions\x12,\n\x08subRooms\x18\x16 \x03(\x0b\x32\x1a.common.Room.SubRoomsEntry\x12\x10\n\x08parentId\x18\x02 \x01(\t\x12\x17\n\x0f\x61llowSpectators\x18\x07 \x01(\x08\x12\x0c\n\x04sort\x18\x08 \x01(\x12\x12*\n\rmyPermissions\x18( \x01(\x0b\x32\x13.common.Permissions\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1aG\n\x10PermissionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\"\n\x05value\x18\x02 \x01(\x0b\x32\x13.common.Permissions:\x02\x38\x01\x1a@\n\rSubRoomsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1e\n\x05value\x18\x02 \x01(\x0b\x32\x0f.common.SubRoom:\x02\x38\x01J\x04\x08\x05\x10\x06R\x04host\"H\n\x07SubRoom\x12\x13\n\x0b\x64isplayName\x18\x03 \x01(\t\x12\x0c\n\x04sort\x18\x04 \x01(\r\x12\x0e\n\x06remove\x18\x05 \x01(\x08\x12\n\n\x02id\x18\x06 \x01(\t\"E\n\nRoomQuotas\x12\x1a\n\x12\x61\x63tiveParticipants\x18\x02 \x01(\r\x12\x1b\n\x13passiveParticipants\x18\x03 \x01(\r*L\n\x08RoomType\x12\x12\n\x0eROOM_TYPE_KEEP\x10\x00\x12\x18\n\x14ROOM_TYPE_DEPARTMENT\x10\x01\x12\x12\n\x0eROOM_TYPE_ROOM\x10\x02*a\n\x08RoomMode\x12\x12\n\x0eROOM_MODE_KEEP\x10\x00\x12\x14\n\x10ROOM_MODE_NORMAL\x10\x01\x12\x12\n\x0eROOM_MODE_EXAM\x10\x02\x12\x17\n\x13ROOM_MODE_SPECTATOR\x10\x03\x62\x06proto3'
  ,
  dependencies=[common_dot_permissions__pb2.DESCRIPTOR,])

_ROOMTYPE = _descriptor.EnumDescriptor(
  name='RoomType',
  full_name='common.RoomType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ROOM_TYPE_KEEP', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROOM_TYPE_DEPARTMENT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROOM_TYPE_ROOM', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=824,
  serialized_end=900,
)
_sym_db.RegisterEnumDescriptor(_ROOMTYPE)

RoomType = enum_type_wrapper.EnumTypeWrapper(_ROOMTYPE)
_ROOMMODE = _descriptor.EnumDescriptor(
  name='RoomMode',
  full_name='common.RoomMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ROOM_MODE_KEEP', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROOM_MODE_NORMAL', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROOM_MODE_EXAM', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROOM_MODE_SPECTATOR', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=902,
  serialized_end=999,
)
_sym_db.RegisterEnumDescriptor(_ROOMMODE)

RoomMode = enum_type_wrapper.EnumTypeWrapper(_ROOMMODE)
ROOM_TYPE_KEEP = 0
ROOM_TYPE_DEPARTMENT = 1
ROOM_TYPE_ROOM = 2
ROOM_MODE_KEEP = 0
ROOM_MODE_NORMAL = 1
ROOM_MODE_EXAM = 2
ROOM_MODE_SPECTATOR = 3



_ROOM_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='common.Room.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='common.Room.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='common.Room.MetadataEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=479,
  serialized_end=526,
)

_ROOM_PERMISSIONSENTRY = _descriptor.Descriptor(
  name='PermissionsEntry',
  full_name='common.Room.PermissionsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='common.Room.PermissionsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='common.Room.PermissionsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=528,
  serialized_end=599,
)

_ROOM_SUBROOMSENTRY = _descriptor.Descriptor(
  name='SubRoomsEntry',
  full_name='common.Room.SubRoomsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='common.Room.SubRoomsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='common.Room.SubRoomsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=601,
  serialized_end=665,
)

_ROOM = _descriptor.Descriptor(
  name='Room',
  full_name='common.Room',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='displayName', full_name='common.Room.displayName', index=0,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mode', full_name='common.Room.mode', index=1,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quotas', full_name='common.Room.quotas', index=2,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='common.Room.type', index=3,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='common.Room.metadata', index=4,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='permissions', full_name='common.Room.permissions', index=5,
      number=20, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='defaultPermissions', full_name='common.Room.defaultPermissions', index=6,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subRooms', full_name='common.Room.subRooms', index=7,
      number=22, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parentId', full_name='common.Room.parentId', index=8,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='allowSpectators', full_name='common.Room.allowSpectators', index=9,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sort', full_name='common.Room.sort', index=10,
      number=8, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='myPermissions', full_name='common.Room.myPermissions', index=11,
      number=40, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ROOM_METADATAENTRY, _ROOM_PERMISSIONSENTRY, _ROOM_SUBROOMSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=56,
  serialized_end=677,
)


_SUBROOM = _descriptor.Descriptor(
  name='SubRoom',
  full_name='common.SubRoom',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='displayName', full_name='common.SubRoom.displayName', index=0,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sort', full_name='common.SubRoom.sort', index=1,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remove', full_name='common.SubRoom.remove', index=2,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='common.SubRoom.id', index=3,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=679,
  serialized_end=751,
)


_ROOMQUOTAS = _descriptor.Descriptor(
  name='RoomQuotas',
  full_name='common.RoomQuotas',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='activeParticipants', full_name='common.RoomQuotas.activeParticipants', index=0,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='passiveParticipants', full_name='common.RoomQuotas.passiveParticipants', index=1,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=753,
  serialized_end=822,
)

_ROOM_METADATAENTRY.containing_type = _ROOM
_ROOM_PERMISSIONSENTRY.fields_by_name['value'].message_type = common_dot_permissions__pb2._PERMISSIONS
_ROOM_PERMISSIONSENTRY.containing_type = _ROOM
_ROOM_SUBROOMSENTRY.fields_by_name['value'].message_type = _SUBROOM
_ROOM_SUBROOMSENTRY.containing_type = _ROOM
_ROOM.fields_by_name['mode'].enum_type = _ROOMMODE
_ROOM.fields_by_name['quotas'].message_type = _ROOMQUOTAS
_ROOM.fields_by_name['type'].enum_type = _ROOMTYPE
_ROOM.fields_by_name['metadata'].message_type = _ROOM_METADATAENTRY
_ROOM.fields_by_name['permissions'].message_type = _ROOM_PERMISSIONSENTRY
_ROOM.fields_by_name['defaultPermissions'].message_type = common_dot_permissions__pb2._PERMISSIONS
_ROOM.fields_by_name['subRooms'].message_type = _ROOM_SUBROOMSENTRY
_ROOM.fields_by_name['myPermissions'].message_type = common_dot_permissions__pb2._PERMISSIONS
DESCRIPTOR.message_types_by_name['Room'] = _ROOM
DESCRIPTOR.message_types_by_name['SubRoom'] = _SUBROOM
DESCRIPTOR.message_types_by_name['RoomQuotas'] = _ROOMQUOTAS
DESCRIPTOR.enum_types_by_name['RoomType'] = _ROOMTYPE
DESCRIPTOR.enum_types_by_name['RoomMode'] = _ROOMMODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Room = _reflection.GeneratedProtocolMessageType('Room', (_message.Message,), {

  'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _ROOM_METADATAENTRY,
    '__module__' : 'common.room_pb2'
    # @@protoc_insertion_point(class_scope:common.Room.MetadataEntry)
    })
  ,

  'PermissionsEntry' : _reflection.GeneratedProtocolMessageType('PermissionsEntry', (_message.Message,), {
    'DESCRIPTOR' : _ROOM_PERMISSIONSENTRY,
    '__module__' : 'common.room_pb2'
    # @@protoc_insertion_point(class_scope:common.Room.PermissionsEntry)
    })
  ,

  'SubRoomsEntry' : _reflection.GeneratedProtocolMessageType('SubRoomsEntry', (_message.Message,), {
    'DESCRIPTOR' : _ROOM_SUBROOMSENTRY,
    '__module__' : 'common.room_pb2'
    # @@protoc_insertion_point(class_scope:common.Room.SubRoomsEntry)
    })
  ,
  'DESCRIPTOR' : _ROOM,
  '__module__' : 'common.room_pb2'
  # @@protoc_insertion_point(class_scope:common.Room)
  })
_sym_db.RegisterMessage(Room)
_sym_db.RegisterMessage(Room.MetadataEntry)
_sym_db.RegisterMessage(Room.PermissionsEntry)
_sym_db.RegisterMessage(Room.SubRoomsEntry)

SubRoom = _reflection.GeneratedProtocolMessageType('SubRoom', (_message.Message,), {
  'DESCRIPTOR' : _SUBROOM,
  '__module__' : 'common.room_pb2'
  # @@protoc_insertion_point(class_scope:common.SubRoom)
  })
_sym_db.RegisterMessage(SubRoom)

RoomQuotas = _reflection.GeneratedProtocolMessageType('RoomQuotas', (_message.Message,), {
  'DESCRIPTOR' : _ROOMQUOTAS,
  '__module__' : 'common.room_pb2'
  # @@protoc_insertion_point(class_scope:common.RoomQuotas)
  })
_sym_db.RegisterMessage(RoomQuotas)


_ROOM_METADATAENTRY._options = None
_ROOM_PERMISSIONSENTRY._options = None
_ROOM_SUBROOMSENTRY._options = None
# @@protoc_insertion_point(module_scope)
