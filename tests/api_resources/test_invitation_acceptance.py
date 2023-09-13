# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from wootiv import Wootiv, AsyncWootiv

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestInvitationAcceptance:
    strict_client = Wootiv(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Wootiv(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: Wootiv) -> None:
        invitation_acceptance = client.invitation_acceptance.retrieve(
            "string",
            passcode="string",
        )
        assert invitation_acceptance is None

    @parametrize
    def test_method_update(self, client: Wootiv) -> None:
        invitation_acceptance = client.invitation_acceptance.update(
            "string",
            passcode="string",
            payload={},
        )
        assert invitation_acceptance is None


class TestAsyncInvitationAcceptance:
    strict_client = AsyncWootiv(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncWootiv(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncWootiv) -> None:
        invitation_acceptance = await client.invitation_acceptance.retrieve(
            "string",
            passcode="string",
        )
        assert invitation_acceptance is None

    @parametrize
    async def test_method_update(self, client: AsyncWootiv) -> None:
        invitation_acceptance = await client.invitation_acceptance.update(
            "string",
            passcode="string",
            payload={},
        )
        assert invitation_acceptance is None
