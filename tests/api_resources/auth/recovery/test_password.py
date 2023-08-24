# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from tecmie import Tecmie, AsyncTecmie

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestPassword:
    strict_client = Tecmie(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Tecmie(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Tecmie) -> None:
        password = client.auth.recovery.password.create(
            email="string",
        )
        assert password is None

    @parametrize
    def test_method_update(self, client: Tecmie) -> None:
        password = client.auth.recovery.password.update(
            new_password="string",
            passcode="string",
        )
        assert password is None


class TestAsyncPassword:
    strict_client = AsyncTecmie(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncTecmie(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncTecmie) -> None:
        password = await client.auth.recovery.password.create(
            email="string",
        )
        assert password is None

    @parametrize
    async def test_method_update(self, client: AsyncTecmie) -> None:
        password = await client.auth.recovery.password.update(
            new_password="string",
            passcode="string",
        )
        assert password is None
