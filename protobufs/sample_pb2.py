# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sample.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0csample.proto\"E\n\x04\x43ity\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07pincode\x18\x02 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x03 \x01(\t\x12\r\n\x05phone\x18\x04 \x03(\tb\x06proto3')



_CITY = DESCRIPTOR.message_types_by_name['City']
City = _reflection.GeneratedProtocolMessageType('City', (_message.Message,), {
  'DESCRIPTOR' : _CITY,
  '__module__' : 'sample_pb2'
  # @@protoc_insertion_point(class_scope:City)
  })
_sym_db.RegisterMessage(City)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CITY._serialized_start=16
  _CITY._serialized_end=85
# @@protoc_insertion_point(module_scope)
