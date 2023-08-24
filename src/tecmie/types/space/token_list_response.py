# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..workspace_dto import WorkspaceDto

__all__ = ["TokenListResponse"]


class Token(BaseModel):
    id: str
    """The unique identifier of the workspace token"""

    audit: object
    """Audit information including timestamps and versions"""

    name: str
    """The human name of the workspace token"""

    sensitive_key: str = FieldInfo(alias="sensitiveKey")
    """The sensitive key truncated that we output"""

    workspace_id: str = FieldInfo(alias="workspaceId")
    """The workspace ID associated with the token"""

    api_key: Optional[str] = FieldInfo(alias="apiKey", default=None)
    """The api key for this account"""

    error_count: Optional[float] = FieldInfo(alias="errorCount", default=None)

    last_error_timestamp: Optional[datetime] = FieldInfo(alias="lastErrorTimestamp", default=None)

    last_request_time_stamp: Optional[datetime] = FieldInfo(alias="lastRequestTimeStamp", default=None)

    request_count: Optional[float] = FieldInfo(alias="requestCount", default=None)

    workspace: Optional[WorkspaceDto] = None
    """The workspace token entity relationship"""


TokenListResponse = List[Token]
