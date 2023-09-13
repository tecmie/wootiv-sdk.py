# File generated from our OpenAPI spec by Stainless.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AwsS3GetOneBucketObjectResponse"]


class AwsS3GetOneBucketObjectResponse(BaseModel):
    signed_url: str = FieldInfo(alias="signedUrl")
    """A signed url to access the object"""
