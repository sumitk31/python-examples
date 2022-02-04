# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: add.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='add.proto',
  package='addrpc',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\tadd.proto\x12\x06\x61\x64\x64rpc\"\x1f\n\x07Numbers\x12\t\n\x01\x61\x18\x01 \x01(\x05\x12\t\n\x01\x62\x18\x02 \x01(\x05\"\x18\n\tAddResult\x12\x0b\n\x03sum\x18\x01 \x01(\x05\x32;\n\x03\x41\x64\x64\x12\x34\n\x0cGetAddResult\x12\x0f.addrpc.Numbers\x1a\x11.addrpc.AddResult\"\x00\x62\x06proto3'
)




_NUMBERS = _descriptor.Descriptor(
  name='Numbers',
  full_name='addrpc.Numbers',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='addrpc.Numbers.a', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='b', full_name='addrpc.Numbers.b', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=21,
  serialized_end=52,
)


_ADDRESULT = _descriptor.Descriptor(
  name='AddResult',
  full_name='addrpc.AddResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sum', full_name='addrpc.AddResult.sum', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=54,
  serialized_end=78,
)

DESCRIPTOR.message_types_by_name['Numbers'] = _NUMBERS
DESCRIPTOR.message_types_by_name['AddResult'] = _ADDRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Numbers = _reflection.GeneratedProtocolMessageType('Numbers', (_message.Message,), {
  'DESCRIPTOR' : _NUMBERS,
  '__module__' : 'add_pb2'
  # @@protoc_insertion_point(class_scope:addrpc.Numbers)
  })
_sym_db.RegisterMessage(Numbers)

AddResult = _reflection.GeneratedProtocolMessageType('AddResult', (_message.Message,), {
  'DESCRIPTOR' : _ADDRESULT,
  '__module__' : 'add_pb2'
  # @@protoc_insertion_point(class_scope:addrpc.AddResult)
  })
_sym_db.RegisterMessage(AddResult)



_ADD = _descriptor.ServiceDescriptor(
  name='Add',
  full_name='addrpc.Add',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=80,
  serialized_end=139,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetAddResult',
    full_name='addrpc.Add.GetAddResult',
    index=0,
    containing_service=None,
    input_type=_NUMBERS,
    output_type=_ADDRESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ADD)

DESCRIPTOR.services_by_name['Add'] = _ADD

# @@protoc_insertion_point(module_scope)
