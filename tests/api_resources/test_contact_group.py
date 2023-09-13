# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from wootiv import Wootiv, AsyncWootiv
from tests.utils import assert_matches_type
from wootiv.types import ReadContactGroupDto, ContactGroupListResponse

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestContactGroup:
    strict_client = Wootiv(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Wootiv(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Wootiv) -> None:
        contact_group = client.contact_group.create(
            group_name="string",
            workspace_id="string",
        )
        assert_matches_type(ReadContactGroupDto, contact_group, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Wootiv) -> None:
        contact_group = client.contact_group.retrieve(
            "string",
        )
        assert_matches_type(ReadContactGroupDto, contact_group, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Wootiv) -> None:
        contact_group = client.contact_group.retrieve(
            "string",
            cache=0,
            fields=["string", "string", "string"],
            join=["string", "string", "string"],
        )
        assert_matches_type(ReadContactGroupDto, contact_group, path=["response"])

    @parametrize
    def test_method_update(self, client: Wootiv) -> None:
        contact_group = client.contact_group.update(
            "string",
            group_name="string",
            workspace_id="string",
        )
        assert_matches_type(ReadContactGroupDto, contact_group, path=["response"])

    @parametrize
    def test_method_list(self, client: Wootiv) -> None:
        contact_group = client.contact_group.list()
        assert_matches_type(ContactGroupListResponse, contact_group, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Wootiv) -> None:
        contact_group = client.contact_group.list(
            cache=0,
            fields=["string", "string", "string"],
            filter=["string", "string", "string"],
            join=["string", "string", "string"],
            limit=0,
            offset=0,
            or_=["string", "string", "string"],
            page=0,
            s="string",
            sort=["string", "string", "string"],
        )
        assert_matches_type(ContactGroupListResponse, contact_group, path=["response"])

    @parametrize
    def test_method_delete(self, client: Wootiv) -> None:
        contact_group = client.contact_group.delete(
            "string",
        )
        assert_matches_type(object, contact_group, path=["response"])


class TestAsyncContactGroup:
    strict_client = AsyncWootiv(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncWootiv(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncWootiv) -> None:
        contact_group = await client.contact_group.create(
            group_name="string",
            workspace_id="string",
        )
        assert_matches_type(ReadContactGroupDto, contact_group, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncWootiv) -> None:
        contact_group = await client.contact_group.retrieve(
            "string",
        )
        assert_matches_type(ReadContactGroupDto, contact_group, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, client: AsyncWootiv) -> None:
        contact_group = await client.contact_group.retrieve(
            "string",
            cache=0,
            fields=["string", "string", "string"],
            join=["string", "string", "string"],
        )
        assert_matches_type(ReadContactGroupDto, contact_group, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncWootiv) -> None:
        contact_group = await client.contact_group.update(
            "string",
            group_name="string",
            workspace_id="string",
        )
        assert_matches_type(ReadContactGroupDto, contact_group, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncWootiv) -> None:
        contact_group = await client.contact_group.list()
        assert_matches_type(ContactGroupListResponse, contact_group, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncWootiv) -> None:
        contact_group = await client.contact_group.list(
            cache=0,
            fields=["string", "string", "string"],
            filter=["string", "string", "string"],
            join=["string", "string", "string"],
            limit=0,
            offset=0,
            or_=["string", "string", "string"],
            page=0,
            s="string",
            sort=["string", "string", "string"],
        )
        assert_matches_type(ContactGroupListResponse, contact_group, path=["response"])

    @parametrize
    async def test_method_delete(self, client: AsyncWootiv) -> None:
        contact_group = await client.contact_group.delete(
            "string",
        )
        assert_matches_type(object, contact_group, path=["response"])
