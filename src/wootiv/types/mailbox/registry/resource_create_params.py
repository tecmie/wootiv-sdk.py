# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ResourceCreateParams"]


class ResourceCreateParams(TypedDict, total=False):
    enabled: Required[bool]
    """Whether the mailbox registry entry is enabled or disabled."""

    name: Required[str]
    """The name of the mailbox registry."""

    raw_content: Required[Annotated[Optional[str], PropertyInfo(alias="rawContent")]]
    """The raw content of the mailbox registry."""

    raw_parsed: Required[Annotated[Optional[str], PropertyInfo(alias="rawParsed")]]
    """The parsed content of the mailbox registry."""

    value: Required[object]
    """The required values needed to setup this registry entry."""
