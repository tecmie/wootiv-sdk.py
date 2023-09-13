# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from wootiv import Wootiv, AsyncWootiv
from tests.utils import assert_matches_type
from wootiv.types import AwsS3GetSignedURLResponse

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestAws:
    strict_client = Wootiv(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Wootiv(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create_signed_put_url(self, client: Wootiv) -> None:
        aw = client.aws.create_signed_put_url(
            filename="sunshine.png",
        )
        assert_matches_type(AwsS3GetSignedURLResponse, aw, path=["response"])


class TestAsyncAws:
    strict_client = AsyncWootiv(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncWootiv(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create_signed_put_url(self, client: AsyncWootiv) -> None:
        aw = await client.aws.create_signed_put_url(
            filename="sunshine.png",
        )
        assert_matches_type(AwsS3GetSignedURLResponse, aw, path=["response"])
