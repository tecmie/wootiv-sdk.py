# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["StreamCreateParams"]


class StreamCreateParams(TypedDict, total=False):
    id: Required[str]

    attachments: Required[Annotated[List[List[object]], PropertyInfo(alias="Attachments")]]

    medium_integration_name: Required[
        Annotated[Literal["whatsapp", "postmark", "twilio", "core_api"], PropertyInfo(alias="mediumIntegrationName")]
    ]

    message_html: Required[Annotated[str, PropertyInfo(alias="messageHTML")]]

    message_text: Required[Annotated[str, PropertyInfo(alias="messageText")]]

    sender: Required[Literal["system", "recipient", "manager", "agent"]]

    status: Required[Literal["sent", "received", "drafted", "flagged", "quarantined", "deleted", "enqueue"]]
