# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from wootiv import Wootiv, AsyncWootiv

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestMembers:
    strict_client = Wootiv(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Wootiv(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: Wootiv) -> None:
        member = client.space.members.retrieve(
            "string",
            space_id="string",
        )
        assert member is None

    @parametrize
    def test_method_list(self, client: Wootiv) -> None:
        member = client.space.members.list(
            "string",
        )
        assert member is None


class TestAsyncMembers:
    strict_client = AsyncWootiv(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncWootiv(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncWootiv) -> None:
        member = await client.space.members.retrieve(
            "string",
            space_id="string",
        )
        assert member is None

    @parametrize
    async def test_method_list(self, client: AsyncWootiv) -> None:
        member = await client.space.members.list(
            "string",
        )
        assert member is None
