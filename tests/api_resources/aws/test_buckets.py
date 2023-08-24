# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from tecmie import Tecmie, AsyncTecmie
from tests.utils import assert_matches_type
from tecmie.types.aws import (
    AwsS3Serialization,
    BucketBulkUploadResponse,
    AwsS3GetOneBucketObjectResponse,
    AwsS3GetManyBucketsSerialization,
)

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestBuckets:
    strict_client = Tecmie(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Tecmie(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_list(self, client: Tecmie) -> None:
        bucket = client.aws.buckets.list()
        assert_matches_type(AwsS3GetManyBucketsSerialization, bucket, path=["response"])

    @parametrize
    def test_method_bulk_upload(self, client: Tecmie) -> None:
        bucket = client.aws.buckets.bulk_upload()
        assert_matches_type(BucketBulkUploadResponse, bucket, path=["response"])

    @parametrize
    def test_method_bulk_upload_with_all_params(self, client: Tecmie) -> None:
        bucket = client.aws.buckets.bulk_upload(
            bulk=[b"raw file contents", b"raw file contents", b"raw file contents"],
            path="string",
        )
        assert_matches_type(BucketBulkUploadResponse, bucket, path=["response"])

    @parametrize
    def test_method_retrieve_file(self, client: Tecmie) -> None:
        bucket = client.aws.buckets.retrieve_file(
            "string",
        )
        assert_matches_type(AwsS3GetOneBucketObjectResponse, bucket, path=["response"])

    @parametrize
    def test_method_retrieve_file_in_path(self, client: Tecmie) -> None:
        bucket = client.aws.buckets.retrieve_file_in_path(
            "string",
            pathname="string",
        )
        assert_matches_type(AwsS3GetOneBucketObjectResponse, bucket, path=["response"])

    @parametrize
    def test_method_upload(self, client: Tecmie) -> None:
        bucket = client.aws.buckets.upload()
        assert_matches_type(AwsS3Serialization, bucket, path=["response"])

    @parametrize
    def test_method_upload_with_all_params(self, client: Tecmie) -> None:
        bucket = client.aws.buckets.upload(
            file=b"raw file contents",
            path="string",
        )
        assert_matches_type(AwsS3Serialization, bucket, path=["response"])


class TestAsyncBuckets:
    strict_client = AsyncTecmie(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncTecmie(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_list(self, client: AsyncTecmie) -> None:
        bucket = await client.aws.buckets.list()
        assert_matches_type(AwsS3GetManyBucketsSerialization, bucket, path=["response"])

    @parametrize
    async def test_method_bulk_upload(self, client: AsyncTecmie) -> None:
        bucket = await client.aws.buckets.bulk_upload()
        assert_matches_type(BucketBulkUploadResponse, bucket, path=["response"])

    @parametrize
    async def test_method_bulk_upload_with_all_params(self, client: AsyncTecmie) -> None:
        bucket = await client.aws.buckets.bulk_upload(
            bulk=[b"raw file contents", b"raw file contents", b"raw file contents"],
            path="string",
        )
        assert_matches_type(BucketBulkUploadResponse, bucket, path=["response"])

    @parametrize
    async def test_method_retrieve_file(self, client: AsyncTecmie) -> None:
        bucket = await client.aws.buckets.retrieve_file(
            "string",
        )
        assert_matches_type(AwsS3GetOneBucketObjectResponse, bucket, path=["response"])

    @parametrize
    async def test_method_retrieve_file_in_path(self, client: AsyncTecmie) -> None:
        bucket = await client.aws.buckets.retrieve_file_in_path(
            "string",
            pathname="string",
        )
        assert_matches_type(AwsS3GetOneBucketObjectResponse, bucket, path=["response"])

    @parametrize
    async def test_method_upload(self, client: AsyncTecmie) -> None:
        bucket = await client.aws.buckets.upload()
        assert_matches_type(AwsS3Serialization, bucket, path=["response"])

    @parametrize
    async def test_method_upload_with_all_params(self, client: AsyncTecmie) -> None:
        bucket = await client.aws.buckets.upload(
            file=b"raw file contents",
            path="string",
        )
        assert_matches_type(AwsS3Serialization, bucket, path=["response"])
