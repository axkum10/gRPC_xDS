# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: echo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\necho.proto\x12\x04\x65\x63ho\"\x1b\n\x0b\x45\x63hoRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1c\n\tEchoReply\x12\x0f\n\x07message\x18\x01 \x01(\t2x\n\nEchoServer\x12\x30\n\x08SayHello\x12\x11.echo.EchoRequest\x1a\x0f.echo.EchoReply\"\x00\x12\x38\n\x0eSayHelloStream\x12\x11.echo.EchoRequest\x1a\x0f.echo.EchoReply\"\x00\x30\x01\x42\x16Z\x14\x65xample.com/app/echob\x06proto3')



_ECHOREQUEST = DESCRIPTOR.message_types_by_name['EchoRequest']
_ECHOREPLY = DESCRIPTOR.message_types_by_name['EchoReply']
EchoRequest = _reflection.GeneratedProtocolMessageType('EchoRequest', (_message.Message,), {
  'DESCRIPTOR' : _ECHOREQUEST,
  '__module__' : 'echo_pb2'
  # @@protoc_insertion_point(class_scope:echo.EchoRequest)
  })
_sym_db.RegisterMessage(EchoRequest)

EchoReply = _reflection.GeneratedProtocolMessageType('EchoReply', (_message.Message,), {
  'DESCRIPTOR' : _ECHOREPLY,
  '__module__' : 'echo_pb2'
  # @@protoc_insertion_point(class_scope:echo.EchoReply)
  })
_sym_db.RegisterMessage(EchoReply)

_ECHOSERVER = DESCRIPTOR.services_by_name['EchoServer']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\024example.com/app/echo'
  _ECHOREQUEST._serialized_start=20
  _ECHOREQUEST._serialized_end=47
  _ECHOREPLY._serialized_start=49
  _ECHOREPLY._serialized_end=77
  _ECHOSERVER._serialized_start=79
  _ECHOSERVER._serialized_end=199
# @@protoc_insertion_point(module_scope)
