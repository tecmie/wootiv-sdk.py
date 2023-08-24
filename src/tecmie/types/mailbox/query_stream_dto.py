# File generated from our OpenAPI spec by Stainless.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["QueryStreamDto"]


class QueryStreamDto(BaseModel):
    id: float

    contact_id: str = FieldInfo(alias="contactId")

    contact_metadata: object = FieldInfo(alias="contactMetadata")

    conversations: object

    mailbox: object

    medium: Literal["sms", "email", "slack", "whatsapp", "facebook", "twitter", "telegram", "discord", "wechat"]

    namespace: str

    pipeline_id: str = FieldInfo(alias="pipelineId")

    slug: str

    status: Literal["open", "composing", "closed", "archived", "quarantined", "spam", "trash"]

    stream_registries: object = FieldInfo(alias="streamRegistries")

    subject: str

    workspace: object

    workspace_id: str = FieldInfo(alias="workspaceId")
