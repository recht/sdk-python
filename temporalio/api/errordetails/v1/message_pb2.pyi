"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import temporalio.api.common.v1.message_pb2
import temporalio.api.enums.v1.failed_cause_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class NotFoundFailure(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CURRENT_CLUSTER_FIELD_NUMBER: builtins.int
    ACTIVE_CLUSTER_FIELD_NUMBER: builtins.int
    current_cluster: typing.Text
    active_cluster: typing.Text
    def __init__(
        self,
        *,
        current_cluster: typing.Text = ...,
        active_cluster: typing.Text = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "active_cluster", b"active_cluster", "current_cluster", b"current_cluster"
        ],
    ) -> None: ...

global___NotFoundFailure = NotFoundFailure

class WorkflowExecutionAlreadyStartedFailure(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    START_REQUEST_ID_FIELD_NUMBER: builtins.int
    RUN_ID_FIELD_NUMBER: builtins.int
    start_request_id: typing.Text
    run_id: typing.Text
    def __init__(
        self,
        *,
        start_request_id: typing.Text = ...,
        run_id: typing.Text = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "run_id", b"run_id", "start_request_id", b"start_request_id"
        ],
    ) -> None: ...

global___WorkflowExecutionAlreadyStartedFailure = WorkflowExecutionAlreadyStartedFailure

class NamespaceNotActiveFailure(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAMESPACE_FIELD_NUMBER: builtins.int
    CURRENT_CLUSTER_FIELD_NUMBER: builtins.int
    ACTIVE_CLUSTER_FIELD_NUMBER: builtins.int
    namespace: typing.Text
    current_cluster: typing.Text
    active_cluster: typing.Text
    def __init__(
        self,
        *,
        namespace: typing.Text = ...,
        current_cluster: typing.Text = ...,
        active_cluster: typing.Text = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "active_cluster",
            b"active_cluster",
            "current_cluster",
            b"current_cluster",
            "namespace",
            b"namespace",
        ],
    ) -> None: ...

global___NamespaceNotActiveFailure = NamespaceNotActiveFailure

class ClientVersionNotSupportedFailure(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLIENT_VERSION_FIELD_NUMBER: builtins.int
    CLIENT_NAME_FIELD_NUMBER: builtins.int
    SUPPORTED_VERSIONS_FIELD_NUMBER: builtins.int
    client_version: typing.Text
    client_name: typing.Text
    supported_versions: typing.Text
    def __init__(
        self,
        *,
        client_version: typing.Text = ...,
        client_name: typing.Text = ...,
        supported_versions: typing.Text = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "client_name",
            b"client_name",
            "client_version",
            b"client_version",
            "supported_versions",
            b"supported_versions",
        ],
    ) -> None: ...

global___ClientVersionNotSupportedFailure = ClientVersionNotSupportedFailure

class ServerVersionNotSupportedFailure(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SERVER_VERSION_FIELD_NUMBER: builtins.int
    CLIENT_SUPPORTED_SERVER_VERSIONS_FIELD_NUMBER: builtins.int
    server_version: typing.Text
    client_supported_server_versions: typing.Text
    def __init__(
        self,
        *,
        server_version: typing.Text = ...,
        client_supported_server_versions: typing.Text = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "client_supported_server_versions",
            b"client_supported_server_versions",
            "server_version",
            b"server_version",
        ],
    ) -> None: ...

global___ServerVersionNotSupportedFailure = ServerVersionNotSupportedFailure

class NamespaceAlreadyExistsFailure(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(
        self,
    ) -> None: ...

global___NamespaceAlreadyExistsFailure = NamespaceAlreadyExistsFailure

class CancellationAlreadyRequestedFailure(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(
        self,
    ) -> None: ...

global___CancellationAlreadyRequestedFailure = CancellationAlreadyRequestedFailure

class QueryFailedFailure(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(
        self,
    ) -> None: ...

global___QueryFailedFailure = QueryFailedFailure

class PermissionDeniedFailure(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    REASON_FIELD_NUMBER: builtins.int
    reason: typing.Text
    def __init__(
        self,
        *,
        reason: typing.Text = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["reason", b"reason"]
    ) -> None: ...

global___PermissionDeniedFailure = PermissionDeniedFailure

class ResourceExhaustedFailure(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CAUSE_FIELD_NUMBER: builtins.int
    cause: temporalio.api.enums.v1.failed_cause_pb2.ResourceExhaustedCause.ValueType
    def __init__(
        self,
        *,
        cause: temporalio.api.enums.v1.failed_cause_pb2.ResourceExhaustedCause.ValueType = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["cause", b"cause"]
    ) -> None: ...

global___ResourceExhaustedFailure = ResourceExhaustedFailure

class SystemWorkflowFailure(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    WORKFLOW_EXECUTION_FIELD_NUMBER: builtins.int
    WORKFLOW_ERROR_FIELD_NUMBER: builtins.int
    @property
    def workflow_execution(
        self,
    ) -> temporalio.api.common.v1.message_pb2.WorkflowExecution:
        """WorkflowId and RunId of the Temporal system workflow performing the underlying operation.
        Looking up the info of the system workflow run may help identify the issue causing the failure.
        """
        pass
    workflow_error: typing.Text
    """Serialized error returned by the system workflow performing the underlying operation."""
    def __init__(
        self,
        *,
        workflow_execution: typing.Optional[
            temporalio.api.common.v1.message_pb2.WorkflowExecution
        ] = ...,
        workflow_error: typing.Text = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "workflow_execution", b"workflow_execution"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "workflow_error",
            b"workflow_error",
            "workflow_execution",
            b"workflow_execution",
        ],
    ) -> None: ...

global___SystemWorkflowFailure = SystemWorkflowFailure