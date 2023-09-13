# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["StreamRegistryQueryDto"]


class StreamRegistryQueryDto(BaseModel):
    id: str
    """The unique identifier of the Stream registry entry."""

    audit: object
    """The audit information for the entity."""

    enabled: bool
    """Whether the Stream registry entry is enabled or disabled."""

    instructions: str
    """The instructions of the Stream registry."""

    name: Literal["cta", "forwarder", "webhook", "calendly", "csv", "pdf", "website", "docx"]
    """The name of the Stream registry."""

    pipeline_id: str = FieldInfo(alias="pipelineId")
    """The ID of the inbox pipeline associated with the Stream registry entry."""

    schema_: object = FieldInfo(alias="schema")
    """The schema associated with the Stream registry entry."""

    source: str
    """The source of the Stream registry."""

    stream_namespace: str = FieldInfo(alias="streamNamespace")
    """The stream namespace associated with the registry entry."""

    type: Literal["action", "tool", "dependency", "resource", "integration", "instruction"]
    """The type of the Stream registry."""

    stream_slug: Optional[str] = FieldInfo(alias="streamSlug", default=None)
    """The stream namespace slug associated with the registry entry."""
