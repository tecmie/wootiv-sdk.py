# File generated from our OpenAPI spec by Stainless.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .shared import AuditDto
from .._models import BaseModel

__all__ = ["SubscriptionDto"]


class SubscriptionDto(BaseModel):
    id: str
    """Subscription ID"""

    audit: AuditDto
    """Audit data"""

    end_date: datetime = FieldInfo(alias="endDate")
    """Subscription end date"""

    history: List[List[object]]

    plan_name: Literal["free", "personal_pro", "business_pro", "enterprise"] = FieldInfo(alias="planName")
    """Subscription Plan Name"""

    start_date: datetime = FieldInfo(alias="startDate")
    """Subscription start date"""

    status: Literal["active", "inactive", "trial", "canceled", "expired"]
    """Subscription status"""

    workspace: object
    """Workspace Associated with this subscription"""

    workspace_id: str = FieldInfo(alias="workspaceId")
    """Unique Workspace ID"""
