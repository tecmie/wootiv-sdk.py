# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from tecmie import Tecmie, AsyncTecmie
from tests.utils import assert_matches_type
from tecmie.types.space import TokenListResponse, TokenCreateResponse

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestTokens:
    strict_client = Tecmie(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Tecmie(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Tecmie) -> None:
        token = client.space.tokens.create(
            "string",
        )
        assert_matches_type(TokenCreateResponse, token, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Tecmie) -> None:
        token = client.space.tokens.create(
            "string",
            name="string",
        )
        assert_matches_type(TokenCreateResponse, token, path=["response"])

    @parametrize
    def test_method_list(self, client: Tecmie) -> None:
        token = client.space.tokens.list(
            "string",
        )
        assert_matches_type(TokenListResponse, token, path=["response"])

    @parametrize
    def test_method_delete(self, client: Tecmie) -> None:
        token = client.space.tokens.delete(
            "string",
            space_sid="string",
        )
        assert token is None


class TestAsyncTokens:
    strict_client = AsyncTecmie(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncTecmie(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncTecmie) -> None:
        token = await client.space.tokens.create(
            "string",
        )
        assert_matches_type(TokenCreateResponse, token, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncTecmie) -> None:
        token = await client.space.tokens.create(
            "string",
            name="string",
        )
        assert_matches_type(TokenCreateResponse, token, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncTecmie) -> None:
        token = await client.space.tokens.list(
            "string",
        )
        assert_matches_type(TokenListResponse, token, path=["response"])

    @parametrize
    async def test_method_delete(self, client: AsyncTecmie) -> None:
        token = await client.space.tokens.delete(
            "string",
            space_sid="string",
        )
        assert token is None
