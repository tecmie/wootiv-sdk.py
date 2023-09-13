# File generated from our OpenAPI spec by Stainless.



from datetime import datetime

from ..._models import BaseModel

__all__ = ["AuditDto"]


class AuditDto(BaseModel):
    date_created: datetime
    """Date created"""

    date_deleted: datetime
    """Date deleted"""

    date_updated: datetime
    """Date updated"""

    version: float
    """Version of the data"""
