# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from wootiv import Wootiv, AsyncWootiv
from tests.utils import assert_matches_type
from wootiv.types import RoleDto, RoleListResponse, RoleBulkCreateResponse

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestRoles:
    strict_client = Wootiv(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Wootiv(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Wootiv) -> None:
        role = client.roles.create(
            description="string",
            name="string",
        )
        assert_matches_type(RoleDto, role, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Wootiv) -> None:
        role = client.roles.retrieve(
            "string",
        )
        assert_matches_type(RoleDto, role, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Wootiv) -> None:
        role = client.roles.retrieve(
            "string",
            cache=0,
            fields=["string", "string", "string"],
            join=["string", "string", "string"],
        )
        assert_matches_type(RoleDto, role, path=["response"])

    @parametrize
    def test_method_update(self, client: Wootiv) -> None:
        role = client.roles.update(
            "string",
            description="string",
            name="string",
        )
        assert_matches_type(RoleDto, role, path=["response"])

    @parametrize
    def test_method_list(self, client: Wootiv) -> None:
        role = client.roles.list()
        assert_matches_type(RoleListResponse, role, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Wootiv) -> None:
        role = client.roles.list(
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
        assert_matches_type(RoleListResponse, role, path=["response"])

    @parametrize
    def test_method_delete(self, client: Wootiv) -> None:
        role = client.roles.delete(
            "string",
        )
        assert_matches_type(object, role, path=["response"])

    @parametrize
    def test_method_bulk_create(self, client: Wootiv) -> None:
        role = client.roles.bulk_create(
            bulk=[
                {
                    "name": "string",
                    "description": "string",
                },
                {
                    "name": "string",
                    "description": "string",
                },
                {
                    "name": "string",
                    "description": "string",
                },
            ],
        )
        assert_matches_type(RoleBulkCreateResponse, role, path=["response"])


class TestAsyncRoles:
    strict_client = AsyncWootiv(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncWootiv(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncWootiv) -> None:
        role = await client.roles.create(
            description="string",
            name="string",
        )
        assert_matches_type(RoleDto, role, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncWootiv) -> None:
        role = await client.roles.retrieve(
            "string",
        )
        assert_matches_type(RoleDto, role, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, client: AsyncWootiv) -> None:
        role = await client.roles.retrieve(
            "string",
            cache=0,
            fields=["string", "string", "string"],
            join=["string", "string", "string"],
        )
        assert_matches_type(RoleDto, role, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncWootiv) -> None:
        role = await client.roles.update(
            "string",
            description="string",
            name="string",
        )
        assert_matches_type(RoleDto, role, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncWootiv) -> None:
        role = await client.roles.list()
        assert_matches_type(RoleListResponse, role, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncWootiv) -> None:
        role = await client.roles.list(
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
        assert_matches_type(RoleListResponse, role, path=["response"])

    @parametrize
    async def test_method_delete(self, client: AsyncWootiv) -> None:
        role = await client.roles.delete(
            "string",
        )
        assert_matches_type(object, role, path=["response"])

    @parametrize
    async def test_method_bulk_create(self, client: AsyncWootiv) -> None:
        role = await client.roles.bulk_create(
            bulk=[
                {
                    "name": "string",
                    "description": "string",
                },
                {
                    "name": "string",
                    "description": "string",
                },
                {
                    "name": "string",
                    "description": "string",
                },
            ],
        )
        assert_matches_type(RoleBulkCreateResponse, role, path=["response"])
