# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/MyService.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/MyService.proto',
  package='MyGrpc',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x15proto/MyService.proto\x12\x06MyGrpc\"\x15\n\x07Request\x12\n\n\x02id\x18\x01 \x01(\x05\"/\n\x0eNameAndSurname\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07surname\x18\x02 \x01(\t2@\n\tMyService\x12\x33\n\x06Search\x12\x0f.MyGrpc.Request\x1a\x16.MyGrpc.NameAndSurname\"\x00\x62\x06proto3')
)




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='MyGrpc.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='MyGrpc.Request.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=33,
  serialized_end=54,
)


_NAMEANDSURNAME = _descriptor.Descriptor(
  name='NameAndSurname',
  full_name='MyGrpc.NameAndSurname',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='MyGrpc.NameAndSurname.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='surname', full_name='MyGrpc.NameAndSurname.surname', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=56,
  serialized_end=103,
)

DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['NameAndSurname'] = _NAMEANDSURNAME
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'proto.MyService_pb2'
  # @@protoc_insertion_point(class_scope:MyGrpc.Request)
  ))
_sym_db.RegisterMessage(Request)

NameAndSurname = _reflection.GeneratedProtocolMessageType('NameAndSurname', (_message.Message,), dict(
  DESCRIPTOR = _NAMEANDSURNAME,
  __module__ = 'proto.MyService_pb2'
  # @@protoc_insertion_point(class_scope:MyGrpc.NameAndSurname)
  ))
_sym_db.RegisterMessage(NameAndSurname)



_MYSERVICE = _descriptor.ServiceDescriptor(
  name='MyService',
  full_name='MyGrpc.MyService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=105,
  serialized_end=169,
  methods=[
  _descriptor.MethodDescriptor(
    name='Search',
    full_name='MyGrpc.MyService.Search',
    index=0,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_NAMEANDSURNAME,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MYSERVICE)

DESCRIPTOR.services_by_name['MyService'] = _MYSERVICE

# @@protoc_insertion_point(module_scope)