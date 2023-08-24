# File generated from our OpenAPI spec by Stainless.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MailboxRegistryQueryDto"]


class MailboxRegistryQueryDto(BaseModel):
    id: str
    """The unique identifier of the mailbox registry entry."""

    audit: object
    """The audit information for the entity."""

    enabled: bool
    """Whether the mailbox registry entry is enabled or disabled."""

    instructions: str
    """The instructions of the mailbox registry."""

    name: Literal["cta", "forwarder", "webhook", "calendly", "csv", "pdf", "website", "docx"]
    """The name of the mailbox registry."""

    pipeline_id: str = FieldInfo(alias="pipelineId")
    """The ID of the inbox pipeline associated with the mailbox registry entry."""

    schema_: object = FieldInfo(alias="schema")
    """The schema associated with the mailbox registry entry."""

    slug: str
    """A lowercase version of our ULID identifier."""

    source: str
    """The source of the mailbox registry."""

    type: Literal["action", "tool", "dependency", "resource", "integration", "instruction"]
    """The type of the mailbox registry."""

    workspace_id: str = FieldInfo(alias="workspaceId")
    """The workspace ID associated with the mailbox registry entry."""
