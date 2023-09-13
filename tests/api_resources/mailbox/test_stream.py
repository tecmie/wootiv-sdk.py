# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from wootiv import Wootiv, AsyncWootiv
from tests.utils import assert_matches_type
from wootiv.types.mailbox import StreamCreateResponse, StreamRetrieveResponse

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestStream:
    strict_client = Wootiv(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Wootiv(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Wootiv) -> None:
        stream = client.mailbox.stream.create(
            "string",
            id="string",
            attachments=[[{}, {}, {}], [{}, {}, {}], [{}, {}, {}]],
            medium_integration_name="whatsapp",
            message_html="string",
            message_text="string",
            sender="system",
            status="sent",
        )
        assert_matches_type(StreamCreateResponse, stream, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Wootiv) -> None:
        stream = client.mailbox.stream.retrieve(
            "string",
            id="string",
        )
        assert_matches_type(StreamRetrieveResponse, stream, path=["response"])


class TestAsyncStream:
    strict_client = AsyncWootiv(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncWootiv(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncWootiv) -> None:
        stream = await client.mailbox.stream.create(
            "string",
            id="string",
            attachments=[[{}, {}, {}], [{}, {}, {}], [{}, {}, {}]],
            medium_integration_name="whatsapp",
            message_html="string",
            message_text="string",
            sender="system",
            status="sent",
        )
        assert_matches_type(StreamCreateResponse, stream, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncWootiv) -> None:
        stream = await client.mailbox.stream.retrieve(
            "string",
            id="string",
        )
        assert_matches_type(StreamRetrieveResponse, stream, path=["response"])
