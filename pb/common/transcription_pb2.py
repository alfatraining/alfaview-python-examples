# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/transcription.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/transcription.proto',
  package='common',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1a\x63ommon/transcription.proto\x12\x06\x63ommon\"Y\n\x15TranscriptionSettings\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12/\n\x08provider\x18\x02 \x01(\x0e\x32\x1d.common.TranscriptionProvider*D\n\x15TranscriptionProvider\x12\x16\n\x12UNDEFINED_PROVIDER\x10\x00\x12\n\n\x06GOOGLE\x10\x01\x12\x07\n\x03KIT\x10\x02\x62\x06proto3')
)

_TRANSCRIPTIONPROVIDER = _descriptor.EnumDescriptor(
  name='TranscriptionProvider',
  full_name='common.TranscriptionProvider',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED_PROVIDER', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GOOGLE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIT', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=129,
  serialized_end=197,
)
_sym_db.RegisterEnumDescriptor(_TRANSCRIPTIONPROVIDER)

TranscriptionProvider = enum_type_wrapper.EnumTypeWrapper(_TRANSCRIPTIONPROVIDER)
UNDEFINED_PROVIDER = 0
GOOGLE = 1
KIT = 2



_TRANSCRIPTIONSETTINGS = _descriptor.Descriptor(
  name='TranscriptionSettings',
  full_name='common.TranscriptionSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enabled', full_name='common.TranscriptionSettings.enabled', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='provider', full_name='common.TranscriptionSettings.provider', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  serialized_start=38,
  serialized_end=127,
)

_TRANSCRIPTIONSETTINGS.fields_by_name['provider'].enum_type = _TRANSCRIPTIONPROVIDER
DESCRIPTOR.message_types_by_name['TranscriptionSettings'] = _TRANSCRIPTIONSETTINGS
DESCRIPTOR.enum_types_by_name['TranscriptionProvider'] = _TRANSCRIPTIONPROVIDER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TranscriptionSettings = _reflection.GeneratedProtocolMessageType('TranscriptionSettings', (_message.Message,), {
  'DESCRIPTOR' : _TRANSCRIPTIONSETTINGS,
  '__module__' : 'common.transcription_pb2'
  # @@protoc_insertion_point(class_scope:common.TranscriptionSettings)
  })
_sym_db.RegisterMessage(TranscriptionSettings)


# @@protoc_insertion_point(module_scope)
