# File generated from our OpenAPI spec by Stainless.

from pydantic import Field as FieldInfo

from .shared import AuditDto
from .._models import BaseModel

__all__ = ["ReadPipelineDto"]


class ReadPipelineDto(BaseModel):
    id: str
    """Unique identifier"""

    audit: AuditDto
    """Audit data"""

    config: object
    """The config schema object of the mailbox"""

    dotcom: str
    """The custom domain suffix for our mailbox address"""

    inbox: str
    """The wootiv mailbox address"""

    name: str
    """The name of the mailbox"""

    objective: str
    """The Objective of this mailbox"""

    status: str
    """The status of the mailbox"""

    unique_address: str = FieldInfo(alias="uniqueAddress")
    """The unique mailbox address of the mailbox"""

    workspace_id: str = FieldInfo(alias="workspaceId")
    """Workspace ID"""
