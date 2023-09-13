# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from wootiv import Wootiv, AsyncWootiv
from tests.utils import assert_matches_type
from wootiv.types import SubscriptionDto
from wootiv._utils import parse_datetime

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestChange:
    strict_client = Wootiv(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Wootiv(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_update(self, client: Wootiv) -> None:
        change = client.subscriptions.change.update(
            path_id="string",
        )
        assert_matches_type(SubscriptionDto, change, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Wootiv) -> None:
        change = client.subscriptions.change.update(
            path_id="string",
            body_id="string",
            audit={
                "date_created": parse_datetime("2019-12-27T18:11:19.117Z"),
                "date_updated": parse_datetime("2019-12-27T18:11:19.117Z"),
                "date_deleted": parse_datetime("2019-12-27T18:11:19.117Z"),
                "version": 0,
            },
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            history=[[{}, {}, {}], [{}, {}, {}], [{}, {}, {}]],
            plan_name="free",
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="active",
            workspace={},
            workspace_id="string",
        )
        assert_matches_type(SubscriptionDto, change, path=["response"])


class TestAsyncChange:
    strict_client = AsyncWootiv(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncWootiv(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_update(self, client: AsyncWootiv) -> None:
        change = await client.subscriptions.change.update(
            path_id="string",
        )
        assert_matches_type(SubscriptionDto, change, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncWootiv) -> None:
        change = await client.subscriptions.change.update(
            path_id="string",
            body_id="string",
            audit={
                "date_created": parse_datetime("2019-12-27T18:11:19.117Z"),
                "date_updated": parse_datetime("2019-12-27T18:11:19.117Z"),
                "date_deleted": parse_datetime("2019-12-27T18:11:19.117Z"),
                "version": 0,
            },
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            history=[[{}, {}, {}], [{}, {}, {}], [{}, {}, {}]],
            plan_name="free",
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="active",
            workspace={},
            workspace_id="string",
        )
        assert_matches_type(SubscriptionDto, change, path=["response"])
