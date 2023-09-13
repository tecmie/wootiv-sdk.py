# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SubscriptionCreateParams"]


class SubscriptionCreateParams(TypedDict, total=False):
    end_date: Required[Annotated[Union[str, datetime], PropertyInfo(alias="endDate", format="iso8601")]]
    """Subscription end date"""

    plan_name: Required[
        Annotated[Literal["free", "personal_pro", "business_pro", "enterprise"], PropertyInfo(alias="planName")]
    ]
    """Subscription Plan Name"""

    start_date: Required[Annotated[Union[str, datetime], PropertyInfo(alias="startDate", format="iso8601")]]
    """Subscription start date"""

    status: Required[Literal["active", "inactive", "trial", "canceled", "expired"]]
    """Subscription status"""

    workspace_id: Required[Annotated[str, PropertyInfo(alias="workspaceId")]]
    """Unique Workspace ID"""
