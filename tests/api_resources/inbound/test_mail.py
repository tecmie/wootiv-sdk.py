# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from wootiv import Wootiv, AsyncWootiv

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestMail:
    strict_client = Wootiv(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Wootiv(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Wootiv) -> None:
        mail = client.inbound.mail.create(
            attachments=[[{}, {}, {}], [{}, {}, {}], [{}, {}, {}]],
            bcc="string",
            bcc_full=[
                {
                    "email": "string",
                    "name": "string",
                    "mailbox_hash": "string",
                },
                {
                    "email": "string",
                    "name": "string",
                    "mailbox_hash": "string",
                },
                {
                    "email": "string",
                    "name": "string",
                    "mailbox_hash": "string",
                },
            ],
            cc="string",
            cc_full=[[{}, {}, {}], [{}, {}, {}], [{}, {}, {}]],
            date="string",
            from_="string",
            from_full={
                "email": "string",
                "name": "string",
                "mailbox_hash": "string",
            },
            from_name="string",
            headers=["string", "string", "string"],
            mailbox_hash="string",
            message_id="string",
            message_stream="string",
            original_recipient="string",
            raw_email="string",
            reply_to="string",
            stripped_text_reply="string",
            subject="string",
            tag="string",
            text_body="string",
            to="string",
            to_full=[
                {
                    "email": "string",
                    "name": "string",
                    "mailbox_hash": "string",
                },
                {
                    "email": "string",
                    "name": "string",
                    "mailbox_hash": "string",
                },
                {
                    "email": "string",
                    "name": "string",
                    "mailbox_hash": "string",
                },
            ],
        )
        assert mail is None


class TestAsyncMail:
    strict_client = AsyncWootiv(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncWootiv(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncWootiv) -> None:
        mail = await client.inbound.mail.create(
            attachments=[[{}, {}, {}], [{}, {}, {}], [{}, {}, {}]],
            bcc="string",
            bcc_full=[
                {
                    "email": "string",
                    "name": "string",
                    "mailbox_hash": "string",
                },
                {
                    "email": "string",
                    "name": "string",
                    "mailbox_hash": "string",
                },
                {
                    "email": "string",
                    "name": "string",
                    "mailbox_hash": "string",
                },
            ],
            cc="string",
            cc_full=[[{}, {}, {}], [{}, {}, {}], [{}, {}, {}]],
            date="string",
            from_="string",
            from_full={
                "email": "string",
                "name": "string",
                "mailbox_hash": "string",
            },
            from_name="string",
            headers=["string", "string", "string"],
            mailbox_hash="string",
            message_id="string",
            message_stream="string",
            original_recipient="string",
            raw_email="string",
            reply_to="string",
            stripped_text_reply="string",
            subject="string",
            tag="string",
            text_body="string",
            to="string",
            to_full=[
                {
                    "email": "string",
                    "name": "string",
                    "mailbox_hash": "string",
                },
                {
                    "email": "string",
                    "name": "string",
                    "mailbox_hash": "string",
                },
                {
                    "email": "string",
                    "name": "string",
                    "mailbox_hash": "string",
                },
            ],
        )
        assert mail is None
