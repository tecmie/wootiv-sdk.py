# File generated from our OpenAPI spec by Stainless.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AwsS3SignedURLPostSerialization"]


class AwsS3SignedURLPostSerialization(BaseModel):
    bucket: str

    policy: str = FieldInfo(alias="Policy")

    x_minus_amz_minus_algorithm: str = FieldInfo(alias="X-Amz-Algorithm")

    x_minus_amz_minus_credential: str = FieldInfo(alias="X-Amz-Credential")

    x_minus_amz_minus_date: str = FieldInfo(alias="X-Amz-Date")

    x_minus_amz_minus_signature: str = FieldInfo(alias="X-Amz-Signature")
