# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from wootiv import Wootiv, AsyncWootiv
from tests.utils import assert_matches_type
from wootiv.types.role_assignments import BulkCreateResponse

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestBulk:
    strict_client = Wootiv(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Wootiv(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Wootiv) -> None:
        bulk = client.role_assignments.bulk.create(
            "string",
            bulk=[
                {
                    "role": {"id": "string"},
                    "assignee": {"id": "string"},
                },
                {
                    "role": {"id": "string"},
                    "assignee": {"id": "string"},
                },
                {
                    "role": {"id": "string"},
                    "assignee": {"id": "string"},
                },
            ],
        )
        assert_matches_type(BulkCreateResponse, bulk, path=["response"])


class TestAsyncBulk:
    strict_client = AsyncWootiv(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncWootiv(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncWootiv) -> None:
        bulk = await client.role_assignments.bulk.create(
            "string",
            bulk=[
                {
                    "role": {"id": "string"},
                    "assignee": {"id": "string"},
                },
                {
                    "role": {"id": "string"},
                    "assignee": {"id": "string"},
                },
                {
                    "role": {"id": "string"},
                    "assignee": {"id": "string"},
                },
            ],
        )
        assert_matches_type(BulkCreateResponse, bulk, path=["response"])
