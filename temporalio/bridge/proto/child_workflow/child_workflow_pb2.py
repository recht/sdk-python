# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: temporal/sdk/core/child_workflow/child_workflow.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from temporalio.api.common.v1 import (
    message_pb2 as temporal_dot_api_dot_common_dot_v1_dot_message__pb2,
)
from temporalio.api.failure.v1 import (
    message_pb2 as temporal_dot_api_dot_failure_dot_v1_dot_message__pb2,
)
from temporalio.bridge.proto.common import (
    common_pb2 as temporal_dot_sdk_dot_core_dot_common_dot_common__pb2,
)

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n5temporal/sdk/core/child_workflow/child_workflow.proto\x12\x16\x63oresdk.child_workflow\x1a$temporal/api/common/v1/message.proto\x1a%temporal/api/failure/v1/message.proto\x1a%temporal/sdk/core/common/common.proto"\xc3\x01\n\x13\x43hildWorkflowResult\x12\x34\n\tcompleted\x18\x01 \x01(\x0b\x32\x1f.coresdk.child_workflow.SuccessH\x00\x12\x31\n\x06\x66\x61iled\x18\x02 \x01(\x0b\x32\x1f.coresdk.child_workflow.FailureH\x00\x12\x39\n\tcancelled\x18\x03 \x01(\x0b\x32$.coresdk.child_workflow.CancellationH\x00\x42\x08\n\x06status":\n\x07Success\x12/\n\x06result\x18\x01 \x01(\x0b\x32\x1f.temporal.api.common.v1.Payload"<\n\x07\x46\x61ilure\x12\x31\n\x07\x66\x61ilure\x18\x01 \x01(\x0b\x32 .temporal.api.failure.v1.Failure"A\n\x0c\x43\x61ncellation\x12\x31\n\x07\x66\x61ilure\x18\x01 \x01(\x0b\x32 .temporal.api.failure.v1.Failure*\xa4\x01\n\x11ParentClosePolicy\x12#\n\x1fPARENT_CLOSE_POLICY_UNSPECIFIED\x10\x00\x12!\n\x1dPARENT_CLOSE_POLICY_TERMINATE\x10\x01\x12\x1f\n\x1bPARENT_CLOSE_POLICY_ABANDON\x10\x02\x12&\n"PARENT_CLOSE_POLICY_REQUEST_CANCEL\x10\x03*\xae\x01\n&StartChildWorkflowExecutionFailedCause\x12;\n7START_CHILD_WORKFLOW_EXECUTION_FAILED_CAUSE_UNSPECIFIED\x10\x00\x12G\nCSTART_CHILD_WORKFLOW_EXECUTION_FAILED_CAUSE_WORKFLOW_ALREADY_EXISTS\x10\x01*~\n\x1d\x43hildWorkflowCancellationType\x12\x0b\n\x07\x41\x42\x41NDON\x10\x00\x12\x0e\n\nTRY_CANCEL\x10\x01\x12\x1f\n\x1bWAIT_CANCELLATION_COMPLETED\x10\x02\x12\x1f\n\x1bWAIT_CANCELLATION_REQUESTED\x10\x03\x62\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "temporal.sdk.core.child_workflow.child_workflow_pb2", globals()
)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _PARENTCLOSEPOLICY._serialized_start = 585
    _PARENTCLOSEPOLICY._serialized_end = 749
    _STARTCHILDWORKFLOWEXECUTIONFAILEDCAUSE._serialized_start = 752
    _STARTCHILDWORKFLOWEXECUTIONFAILEDCAUSE._serialized_end = 926
    _CHILDWORKFLOWCANCELLATIONTYPE._serialized_start = 928
    _CHILDWORKFLOWCANCELLATIONTYPE._serialized_end = 1054
    _CHILDWORKFLOWRESULT._serialized_start = 198
    _CHILDWORKFLOWRESULT._serialized_end = 393
    _SUCCESS._serialized_start = 395
    _SUCCESS._serialized_end = 453
    _FAILURE._serialized_start = 455
    _FAILURE._serialized_end = 515
    _CANCELLATION._serialized_start = 517
    _CANCELLATION._serialized_end = 582
# @@protoc_insertion_point(module_scope)
