# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from tecmie import Tecmie, AsyncTecmie
from tests.utils import assert_matches_type
from tecmie.types import ReadPipelineDto, MailboxListResponse

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestMailbox:
    strict_client = Tecmie(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Tecmie(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Tecmie) -> None:
        mailbox = client.mailbox.create(
            config={},
            dotcom="wootiv.com",
            name="string",
            objective="string",
            unique_address="string",
        )
        assert_matches_type(ReadPipelineDto, mailbox, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Tecmie) -> None:
        mailbox = client.mailbox.create(
            config={},
            dotcom="wootiv.com",
            name="string",
            objective="string",
            unique_address="string",
            workspace_id="string",
        )
        assert_matches_type(ReadPipelineDto, mailbox, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Tecmie) -> None:
        mailbox = client.mailbox.retrieve(
            "string",
        )
        assert_matches_type(ReadPipelineDto, mailbox, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Tecmie) -> None:
        mailbox = client.mailbox.retrieve(
            "string",
            cache=0,
            fields=["string", "string", "string"],
            join=["string", "string", "string"],
        )
        assert_matches_type(ReadPipelineDto, mailbox, path=["response"])

    @parametrize
    def test_method_update(self, client: Tecmie) -> None:
        mailbox = client.mailbox.update(
            "string",
        )
        assert_matches_type(ReadPipelineDto, mailbox, path=["response"])

    @parametrize
    def test_method_list(self, client: Tecmie) -> None:
        mailbox = client.mailbox.list()
        assert_matches_type(MailboxListResponse, mailbox, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Tecmie) -> None:
        mailbox = client.mailbox.list(
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
        assert_matches_type(MailboxListResponse, mailbox, path=["response"])

    @parametrize
    def test_method_delete(self, client: Tecmie) -> None:
        mailbox = client.mailbox.delete(
            "string",
        )
        assert_matches_type(object, mailbox, path=["response"])

    @parametrize
    def test_method_check_availability(self, client: Tecmie) -> None:
        mailbox = client.mailbox.check_availability(
            unique_address="string",
        )
        assert mailbox is None


class TestAsyncMailbox:
    strict_client = AsyncTecmie(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncTecmie(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncTecmie) -> None:
        mailbox = await client.mailbox.create(
            config={},
            dotcom="wootiv.com",
            name="string",
            objective="string",
            unique_address="string",
        )
        assert_matches_type(ReadPipelineDto, mailbox, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncTecmie) -> None:
        mailbox = await client.mailbox.create(
            config={},
            dotcom="wootiv.com",
            name="string",
            objective="string",
            unique_address="string",
            workspace_id="string",
        )
        assert_matches_type(ReadPipelineDto, mailbox, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncTecmie) -> None:
        mailbox = await client.mailbox.retrieve(
            "string",
        )
        assert_matches_type(ReadPipelineDto, mailbox, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, client: AsyncTecmie) -> None:
        mailbox = await client.mailbox.retrieve(
            "string",
            cache=0,
            fields=["string", "string", "string"],
            join=["string", "string", "string"],
        )
        assert_matches_type(ReadPipelineDto, mailbox, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncTecmie) -> None:
        mailbox = await client.mailbox.update(
            "string",
        )
        assert_matches_type(ReadPipelineDto, mailbox, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncTecmie) -> None:
        mailbox = await client.mailbox.list()
        assert_matches_type(MailboxListResponse, mailbox, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncTecmie) -> None:
        mailbox = await client.mailbox.list(
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
        assert_matches_type(MailboxListResponse, mailbox, path=["response"])

    @parametrize
    async def test_method_delete(self, client: AsyncTecmie) -> None:
        mailbox = await client.mailbox.delete(
            "string",
        )
        assert_matches_type(object, mailbox, path=["response"])

    @parametrize
    async def test_method_check_availability(self, client: AsyncTecmie) -> None:
        mailbox = await client.mailbox.check_availability(
            unique_address="string",
        )
        assert mailbox is None
