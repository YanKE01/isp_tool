# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: protocols.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'protocols.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fprotocols.proto\x12\x0bisppipeline\"^\n\x13\x43\x61ptureImageCommand\x12\r\n\x05width\x18\x01 \x01(\r\x12\x0e\n\x06height\x18\x02 \x01(\r\x12(\n\x06\x66ormat\x18\x03 \x01(\x0e\x32\x18.isppipeline.ImageFormat\"\x1a\n\x18ReadISPParametersCommand\"\xad\x01\n\x19WriteISPParametersCommand\x12)\n\x03\x62lc\x18\x01 \x01(\x0b\x32\x1a.isppipeline.BLCParametersH\x00\x12)\n\x03\x63\x63m\x18\x02 \x01(\x0b\x32\x1a.isppipeline.CCMParametersH\x00\x12-\n\x05gamma\x18\x03 \x01(\x0b\x32\x1c.isppipeline.GammaParametersH\x00\x42\x0b\n\tparameter\"Y\n\rBLCParameters\x12\x10\n\x08r_offset\x18\x01 \x01(\x02\x12\x11\n\tgr_offset\x18\x02 \x01(\x02\x12\x11\n\tgb_offset\x18\x03 \x01(\x02\x12\x10\n\x08\x62_offset\x18\x04 \x01(\x02\"-\n\rCCMParameters\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\x0b\n\x03\x63\x63m\x18\x02 \x03(\x02\"1\n\x0fGammaParameters\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\r\n\x05gamma\x18\x02 \x03(\r\"\x8e\x01\n\rISPParameters\x12\'\n\x03\x62lc\x18\x01 \x01(\x0b\x32\x1a.isppipeline.BLCParameters\x12\'\n\x03\x63\x63m\x18\x02 \x01(\x0b\x32\x1a.isppipeline.CCMParameters\x12+\n\x05gamma\x18\x03 \x01(\x0b\x32\x1c.isppipeline.GammaParameters\"h\n\x15ISPParametersResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\x12.\n\nparameters\x18\x03 \x01(\x0b\x32\x1a.isppipeline.ISPParameters\"\x8d\x01\n\rImageResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x12\n\nimage_data\x18\x03 \x01(\x0c\x12\r\n\x05width\x18\x04 \x01(\r\x12\x0e\n\x06height\x18\x05 \x01(\r\x12(\n\x06\x66ormat\x18\x06 \x01(\x0e\x32\x18.isppipeline.ImageFormat\"\xf5\x02\n\nDataPacket\x12\x41\n\x15\x63\x61pture_image_command\x18\x01 \x01(\x0b\x32 .isppipeline.CaptureImageCommandH\x00\x12\x34\n\x0eimage_response\x18\x02 \x01(\x0b\x32\x1a.isppipeline.ImageResponseH\x00\x12L\n\x1bread_isp_parameters_command\x18\x03 \x01(\x0b\x32%.isppipeline.ReadISPParametersCommandH\x00\x12\x45\n\x17isp_parameters_response\x18\x04 \x01(\x0b\x32\".isppipeline.ISPParametersResponseH\x00\x12N\n\x1cwrite_isp_parameters_command\x18\x05 \x01(\x0b\x32&.isppipeline.WriteISPParametersCommandH\x00\x42\t\n\x07payload*B\n\x0bImageFormat\x12\x07\n\x03JPG\x10\x00\x12\x08\n\x04RAW8\x10\x01\x12\t\n\x05RAW10\x10\x02\x12\n\n\x06RGB565\x10\x03\x12\t\n\x05RGB24\x10\x04\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protocols_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_IMAGEFORMAT']._serialized_start=1292
  _globals['_IMAGEFORMAT']._serialized_end=1358
  _globals['_CAPTUREIMAGECOMMAND']._serialized_start=32
  _globals['_CAPTUREIMAGECOMMAND']._serialized_end=126
  _globals['_READISPPARAMETERSCOMMAND']._serialized_start=128
  _globals['_READISPPARAMETERSCOMMAND']._serialized_end=154
  _globals['_WRITEISPPARAMETERSCOMMAND']._serialized_start=157
  _globals['_WRITEISPPARAMETERSCOMMAND']._serialized_end=330
  _globals['_BLCPARAMETERS']._serialized_start=332
  _globals['_BLCPARAMETERS']._serialized_end=421
  _globals['_CCMPARAMETERS']._serialized_start=423
  _globals['_CCMPARAMETERS']._serialized_end=468
  _globals['_GAMMAPARAMETERS']._serialized_start=470
  _globals['_GAMMAPARAMETERS']._serialized_end=519
  _globals['_ISPPARAMETERS']._serialized_start=522
  _globals['_ISPPARAMETERS']._serialized_end=664
  _globals['_ISPPARAMETERSRESPONSE']._serialized_start=666
  _globals['_ISPPARAMETERSRESPONSE']._serialized_end=770
  _globals['_IMAGERESPONSE']._serialized_start=773
  _globals['_IMAGERESPONSE']._serialized_end=914
  _globals['_DATAPACKET']._serialized_start=917
  _globals['_DATAPACKET']._serialized_end=1290
# @@protoc_insertion_point(module_scope)
