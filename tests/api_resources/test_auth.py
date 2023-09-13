# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from wootiv import Wootiv, AsyncWootiv
from tests.utils import assert_matches_type
from wootiv.types import (
    AuthLoginResponse,
    AuthSignupResponse,
    AuthVerifyBillingResponse,
)

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestAuth:
    strict_client = Wootiv(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Wootiv(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_login(self, client: Wootiv) -> None:
        auth = client.auth.login(
            password="string",
            username="string",
        )
        assert_matches_type(AuthLoginResponse, auth, path=["response"])

    @parametrize
    def test_method_signup(self, client: Wootiv) -> None:
        auth = client.auth.signup(
            email="string",
            password="string",
            plan="string",
        )
        assert_matches_type(AuthSignupResponse, auth, path=["response"])

    @parametrize
    def test_method_signup_with_all_params(self, client: Wootiv) -> None:
        auth = client.auth.signup(
            email="string",
            password="string",
            plan="string",
            first_name="string",
            last_name="string",
            phone_number="string",
        )
        assert_matches_type(AuthSignupResponse, auth, path=["response"])

    @parametrize
    def test_method_verify_billing(self, client: Wootiv) -> None:
        auth = client.auth.verify_billing(
            sub="string",
        )
        assert_matches_type(AuthVerifyBillingResponse, auth, path=["response"])


class TestAsyncAuth:
    strict_client = AsyncWootiv(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncWootiv(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_login(self, client: AsyncWootiv) -> None:
        auth = await client.auth.login(
            password="string",
            username="string",
        )
        assert_matches_type(AuthLoginResponse, auth, path=["response"])

    @parametrize
    async def test_method_signup(self, client: AsyncWootiv) -> None:
        auth = await client.auth.signup(
            email="string",
            password="string",
            plan="string",
        )
        assert_matches_type(AuthSignupResponse, auth, path=["response"])

    @parametrize
    async def test_method_signup_with_all_params(self, client: AsyncWootiv) -> None:
        auth = await client.auth.signup(
            email="string",
            password="string",
            plan="string",
            first_name="string",
            last_name="string",
            phone_number="string",
        )
        assert_matches_type(AuthSignupResponse, auth, path=["response"])

    @parametrize
    async def test_method_verify_billing(self, client: AsyncWootiv) -> None:
        auth = await client.auth.verify_billing(
            sub="string",
        )
        assert_matches_type(AuthVerifyBillingResponse, auth, path=["response"])
