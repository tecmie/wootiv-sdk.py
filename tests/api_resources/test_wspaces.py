# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from tecmie import Tecmie, AsyncTecmie
from tests.utils import assert_matches_type
from tecmie.types import WorkspaceDto

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestWspaces:
    strict_client = Tecmie(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Tecmie(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Tecmie) -> None:
        wspace = client.wspaces.create(
            name="string",
            owner_id="string",
        )
        assert_matches_type(WorkspaceDto, wspace, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Tecmie) -> None:
        wspace = client.wspaces.retrieve(
            "string",
        )
        assert_matches_type(WorkspaceDto, wspace, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Tecmie) -> None:
        wspace = client.wspaces.retrieve(
            "string",
            cache=0,
            fields=["string", "string", "string"],
            join=["string", "string", "string"],
        )
        assert_matches_type(WorkspaceDto, wspace, path=["response"])

    @parametrize
    def test_method_update(self, client: Tecmie) -> None:
        wspace = client.wspaces.update(
            "string",
        )
        assert_matches_type(WorkspaceDto, wspace, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Tecmie) -> None:
        wspace = client.wspaces.update(
            "string",
            body_id="string",
            audit={},
            name="string",
            owner_id="string",
            slug="string",
            subscription={},
            subscription_id="string",
            workspace_members=["string", "string", "string"],
        )
        assert_matches_type(WorkspaceDto, wspace, path=["response"])


class TestAsyncWspaces:
    strict_client = AsyncTecmie(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncTecmie(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncTecmie) -> None:
        wspace = await client.wspaces.create(
            name="string",
            owner_id="string",
        )
        assert_matches_type(WorkspaceDto, wspace, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncTecmie) -> None:
        wspace = await client.wspaces.retrieve(
            "string",
        )
        assert_matches_type(WorkspaceDto, wspace, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, client: AsyncTecmie) -> None:
        wspace = await client.wspaces.retrieve(
            "string",
            cache=0,
            fields=["string", "string", "string"],
            join=["string", "string", "string"],
        )
        assert_matches_type(WorkspaceDto, wspace, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncTecmie) -> None:
        wspace = await client.wspaces.update(
            "string",
        )
        assert_matches_type(WorkspaceDto, wspace, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncTecmie) -> None:
        wspace = await client.wspaces.update(
            "string",
            body_id="string",
            audit={},
            name="string",
            owner_id="string",
            slug="string",
            subscription={},
            subscription_id="string",
            workspace_members=["string", "string", "string"],
        )
        assert_matches_type(WorkspaceDto, wspace, path=["response"])
