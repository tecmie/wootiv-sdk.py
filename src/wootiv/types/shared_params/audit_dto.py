# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AuditDto"]


class AuditDto(TypedDict, total=False):
    date_created: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Date created"""

    date_deleted: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Date deleted"""

    date_updated: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Date updated"""

    version: Required[float]
    """Version of the data"""
