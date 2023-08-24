# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...types import shared_params
from ..._utils import PropertyInfo

__all__ = ["ChangeUpdateParams"]


class ChangeUpdateParams(TypedDict, total=False):
    path_id: Required[Annotated[str, PropertyInfo(alias="id")]]

    body_id: Annotated[str, PropertyInfo(alias="id")]
    """Subscription ID"""

    audit: shared_params.AuditDto
    """Audit data"""

    end_date: Annotated[Union[str, datetime], PropertyInfo(alias="endDate", format="iso8601")]
    """Subscription end date"""

    history: List[List[object]]

    plan_name: Annotated[Literal["free", "personal_pro", "business_pro", "enterprise"], PropertyInfo(alias="planName")]
    """Subscription Plan Name"""

    start_date: Annotated[Union[str, datetime], PropertyInfo(alias="startDate", format="iso8601")]
    """Subscription start date"""

    status: Literal["active", "inactive", "trial", "canceled", "expired"]
    """Subscription status"""

    workspace: object
    """Workspace Associated with this subscription"""

    workspace_id: Annotated[str, PropertyInfo(alias="workspaceId")]
    """Unique Workspace ID"""
