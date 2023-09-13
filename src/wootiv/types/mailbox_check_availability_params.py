# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MailboxCheckAvailabilityParams"]


class MailboxCheckAvailabilityParams(TypedDict, total=False):
    unique_address: Required[Annotated[str, PropertyInfo(alias="uniqueAddress")]]
    """The unique address of the pipeline"""
