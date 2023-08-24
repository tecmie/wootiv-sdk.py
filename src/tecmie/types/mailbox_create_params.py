# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MailboxCreateParams"]


class MailboxCreateParams(TypedDict, total=False):
    config: Required[object]

    dotcom: Required[str]
    """The dotcom namespace of the mailbox without the protocol"""

    name: Required[str]
    """name of the pipeline"""

    objective: Required[str]
    """The objective of the pipeline"""

    unique_address: Required[Annotated[str, PropertyInfo(alias="uniqueAddress")]]
    """The unique address of the pipeline"""

    workspace_id: Annotated[str, PropertyInfo(alias="workspaceId")]
    """Workspace ID"""
