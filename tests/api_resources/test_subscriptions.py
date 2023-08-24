# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from tecmie import Tecmie, AsyncTecmie
from tests.utils import assert_matches_type
from tecmie.types import SubscriptionDto
from tecmie._utils import parse_datetime

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestSubscriptions:
    strict_client = Tecmie(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Tecmie(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Tecmie) -> None:
        subscription = client.subscriptions.create(
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            plan_name="free",
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="active",
            workspace_id="string",
        )
        assert_matches_type(SubscriptionDto, subscription, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Tecmie) -> None:
        subscription = client.subscriptions.retrieve(
            "string",
        )
        assert_matches_type(SubscriptionDto, subscription, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Tecmie) -> None:
        subscription = client.subscriptions.retrieve(
            "string",
            cache=0,
            fields=["string", "string", "string"],
            join=["string", "string", "string"],
        )
        assert_matches_type(SubscriptionDto, subscription, path=["response"])

    @parametrize
    def test_method_update(self, client: Tecmie) -> None:
        subscription = client.subscriptions.update(
            "string",
        )
        assert_matches_type(SubscriptionDto, subscription, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Tecmie) -> None:
        subscription = client.subscriptions.update(
            "string",
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
        assert_matches_type(SubscriptionDto, subscription, path=["response"])


class TestAsyncSubscriptions:
    strict_client = AsyncTecmie(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncTecmie(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncTecmie) -> None:
        subscription = await client.subscriptions.create(
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            plan_name="free",
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="active",
            workspace_id="string",
        )
        assert_matches_type(SubscriptionDto, subscription, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncTecmie) -> None:
        subscription = await client.subscriptions.retrieve(
            "string",
        )
        assert_matches_type(SubscriptionDto, subscription, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, client: AsyncTecmie) -> None:
        subscription = await client.subscriptions.retrieve(
            "string",
            cache=0,
            fields=["string", "string", "string"],
            join=["string", "string", "string"],
        )
        assert_matches_type(SubscriptionDto, subscription, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncTecmie) -> None:
        subscription = await client.subscriptions.update(
            "string",
        )
        assert_matches_type(SubscriptionDto, subscription, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncTecmie) -> None:
        subscription = await client.subscriptions.update(
            "string",
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
        assert_matches_type(SubscriptionDto, subscription, path=["response"])
