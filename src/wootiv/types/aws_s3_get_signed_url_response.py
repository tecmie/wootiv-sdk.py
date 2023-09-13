# File generated from our OpenAPI spec by Stainless.

from .._models import BaseModel
from .aws_s3_signed_url_post_serialization import AwsS3SignedURLPostSerialization

__all__ = ["AwsS3GetSignedURLResponse"]


class AwsS3GetSignedURLResponse(BaseModel):
    fields: AwsS3SignedURLPostSerialization

    url: str
