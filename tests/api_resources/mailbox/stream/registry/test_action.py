# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from wootiv import Wootiv, AsyncWootiv
from tests.utils import assert_matches_type
from wootiv.types.mailbox.stream.registry import (
    OneStreamRegistryAction,
    PaginatedStreamRegistry,
)

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestAction:
    strict_client = Wootiv(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Wootiv(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Wootiv) -> None:
        action = client.mailbox.stream.registry.action.create(
            "string",
            id="string",
            enabled=False,
            name="website",
            raw_content="string",
            raw_parsed="string",
            value={"instruction": "An instruction that states when to use this resource or action"},
        )
        assert_matches_type(OneStreamRegistryAction, action, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Wootiv) -> None:
        action = client.mailbox.stream.registry.action.retrieve(
            "string",
            id="string",
        )
        assert_matches_type(PaginatedStreamRegistry, action, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Wootiv) -> None:
        action = client.mailbox.stream.registry.action.retrieve(
            "string",
            id="string",
            limit=0,
            offset=0,
        )
        assert_matches_type(PaginatedStreamRegistry, action, path=["response"])


class TestAsyncAction:
    strict_client = AsyncWootiv(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncWootiv(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncWootiv) -> None:
        action = await client.mailbox.stream.registry.action.create(
            "string",
            id="string",
            enabled=False,
            name="website",
            raw_content="string",
            raw_parsed="string",
            value={"instruction": "An instruction that states when to use this resource or action"},
        )
        assert_matches_type(OneStreamRegistryAction, action, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncWootiv) -> None:
        action = await client.mailbox.stream.registry.action.retrieve(
            "string",
            id="string",
        )
        assert_matches_type(PaginatedStreamRegistry, action, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, client: AsyncWootiv) -> None:
        action = await client.mailbox.stream.registry.action.retrieve(
            "string",
            id="string",
            limit=0,
            offset=0,
        )
        assert_matches_type(PaginatedStreamRegistry, action, path=["response"])
