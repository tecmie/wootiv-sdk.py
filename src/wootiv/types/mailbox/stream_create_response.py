# File generated from our OpenAPI spec by Stainless.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["StreamCreateResponse"]


class StreamCreateResponse(BaseModel):
    id: float

    attachments: List[List[object]] = FieldInfo(alias="Attachments")

    medium_integration_name: str = FieldInfo(alias="mediumIntegrationName")

    message_html: str = FieldInfo(alias="messageHTML")

    message_text: str = FieldInfo(alias="messageText")

    sender: str

    status: str

    stream_namespace: str = FieldInfo(alias="streamNamespace")

    workspace_id: str = FieldInfo(alias="workspaceId")
