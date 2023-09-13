# File generated from our OpenAPI spec by Stainless.

from typing import List

from ..._models import BaseModel

__all__ = ["AwsS3GetManyBucketsSerialization"]


class AwsS3GetManyBucketsSerialization(BaseModel):
    buckets: List[object]
    """A list of all the buckets from the AWS AccessKey"""
