# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from tecmie import Tecmie, AsyncTecmie
from tests.utils import assert_matches_type
from tecmie.types import RoleAssignmentDto

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestRoleAssignments:
    strict_client = Tecmie(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Tecmie(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Tecmie) -> None:
        role_assignment = client.role_assignments.create(
            "string",
            assignee={"id": "string"},
            role={"id": "string"},
        )
        assert_matches_type(RoleAssignmentDto, role_assignment, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Tecmie) -> None:
        role_assignment = client.role_assignments.retrieve(
            "string",
            assignment="string",
        )
        assert_matches_type(RoleAssignmentDto, role_assignment, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Tecmie) -> None:
        role_assignment = client.role_assignments.retrieve(
            "string",
            assignment="string",
            cache=0,
            fields=["string", "string", "string"],
            join=["string", "string", "string"],
        )
        assert_matches_type(RoleAssignmentDto, role_assignment, path=["response"])

    @parametrize
    def test_method_delete(self, client: Tecmie) -> None:
        role_assignment = client.role_assignments.delete(
            "string",
            assignment="string",
        )
        assert_matches_type(object, role_assignment, path=["response"])


class TestAsyncRoleAssignments:
    strict_client = AsyncTecmie(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncTecmie(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncTecmie) -> None:
        role_assignment = await client.role_assignments.create(
            "string",
            assignee={"id": "string"},
            role={"id": "string"},
        )
        assert_matches_type(RoleAssignmentDto, role_assignment, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncTecmie) -> None:
        role_assignment = await client.role_assignments.retrieve(
            "string",
            assignment="string",
        )
        assert_matches_type(RoleAssignmentDto, role_assignment, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, client: AsyncTecmie) -> None:
        role_assignment = await client.role_assignments.retrieve(
            "string",
            assignment="string",
            cache=0,
            fields=["string", "string", "string"],
            join=["string", "string", "string"],
        )
        assert_matches_type(RoleAssignmentDto, role_assignment, path=["response"])

    @parametrize
    async def test_method_delete(self, client: AsyncTecmie) -> None:
        role_assignment = await client.role_assignments.delete(
            "string",
            assignment="string",
        )
        assert_matches_type(object, role_assignment, path=["response"])
