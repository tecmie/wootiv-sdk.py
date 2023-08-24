# File generated from our OpenAPI spec by Stainless.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AwsS3Serialization"]


class AwsS3Serialization(BaseModel):
    base_url: str = FieldInfo(alias="baseUrl")

    filename: str

    mime: str

    path: str

    path_with_filename: str = FieldInfo(alias="pathWithFilename")

    signed_url: str = FieldInfo(alias="signedUrl")
