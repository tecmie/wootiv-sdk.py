# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Any, List, cast

from .stream import Stream, AsyncStream
from ...types import (
    ReadPipelineDto,
    MailboxListResponse,
    mailbox_list_params,
    mailbox_create_params,
    mailbox_retrieve_params,
    mailbox_check_availability_params,
)
from ..._types import (
    NOT_GIVEN,
    Body,
    Query,
    Headers,
    NoneType,
    NotGiven,
    UnknownResponse,
)
from ..._utils import maybe_transform
from .registry import Registry, AsyncRegistry
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options

if TYPE_CHECKING:
    from ..._client import Tecmie, AsyncTecmie

__all__ = ["Mailbox", "AsyncMailbox"]


class Mailbox(SyncAPIResource):
    registry: Registry
    stream: Stream

    def __init__(self, client: Tecmie) -> None:
        super().__init__(client)
        self.registry = Registry(client)
        self.stream = Stream(client)

    def create(
        self,
        *,
        config: object,
        dotcom: str,
        name: str,
        objective: str,
        unique_address: str,
        workspace_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ReadPipelineDto:
        """
        Args:
          dotcom: The dotcom namespace of the mailbox without the protocol

          name: name of the pipeline

          objective: The objective of the pipeline

          uniqueAddress: The unique address of the pipeline

          workspaceId: Workspace ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/mailbox",
            body=maybe_transform(
                {
                    "config": config,
                    "dotcom": dotcom,
                    "name": name,
                    "objective": objective,
                    "unique_address": unique_address,
                    "workspace_id": workspace_id,
                },
                mailbox_create_params.MailboxCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReadPipelineDto,
        )

    def retrieve(
        self,
        id: str,
        *,
        cache: int | NotGiven = NOT_GIVEN,
        fields: List[str] | NotGiven = NOT_GIVEN,
        join: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ReadPipelineDto:
        """
        Args:
          cache: Reset cache (if was enabled).
              <a href="https://github.com/nestjsx/crud/wiki/Requests#cache" target="_blank">Docs</a>

          fields: Selects resource fields.
              <a href="https://github.com/nestjsx/crud/wiki/Requests#select" target="_blank">Docs</a>

          join: Adds relational resources.
              <a href="https://github.com/nestjsx/crud/wiki/Requests#join" target="_blank">Docs</a>

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/mailbox/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cache": cache,
                        "fields": fields,
                        "join": join,
                    },
                    mailbox_retrieve_params.MailboxRetrieveParams,
                ),
            ),
            cast_to=ReadPipelineDto,
        )

    def update(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ReadPipelineDto:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/mailbox/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReadPipelineDto,
        )

    def list(
        self,
        *,
        cache: int | NotGiven = NOT_GIVEN,
        fields: List[str] | NotGiven = NOT_GIVEN,
        filter: List[str] | NotGiven = NOT_GIVEN,
        join: List[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        or_: List[str] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        s: str | NotGiven = NOT_GIVEN,
        sort: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> MailboxListResponse:
        """
        Args:
          cache: Reset cache (if was enabled).
              <a href="https://github.com/nestjsx/crud/wiki/Requests#cache" target="_blank">Docs</a>

          fields: Selects resource fields.
              <a href="https://github.com/nestjsx/crud/wiki/Requests#select" target="_blank">Docs</a>

          filter: Adds filter condition.
              <a href="https://github.com/nestjsx/crud/wiki/Requests#filter" target="_blank">Docs</a>

          join: Adds relational resources.
              <a href="https://github.com/nestjsx/crud/wiki/Requests#join" target="_blank">Docs</a>

          limit: Limit amount of resources.
              <a href="https://github.com/nestjsx/crud/wiki/Requests#limit" target="_blank">Docs</a>

          offset: Offset amount of resources.
              <a href="https://github.com/nestjsx/crud/wiki/Requests#offset" target="_blank">Docs</a>

          or: Adds OR condition.
              <a href="https://github.com/nestjsx/crud/wiki/Requests#or" target="_blank">Docs</a>

          page: Page portion of resources.
              <a href="https://github.com/nestjsx/crud/wiki/Requests#page" target="_blank">Docs</a>

          s: Adds search condition.
              <a href="https://github.com/nestjsx/crud/wiki/Requests#search" target="_blank">Docs</a>

          sort: Adds sort by field.
              <a href="https://github.com/nestjsx/crud/wiki/Requests#sort" target="_blank">Docs</a>

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            MailboxListResponse,
            self._get(
                "/mailbox",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {
                            "cache": cache,
                            "fields": fields,
                            "filter": filter,
                            "join": join,
                            "limit": limit,
                            "offset": offset,
                            "or_": or_,
                            "page": page,
                            "s": s,
                            "sort": sort,
                        },
                        mailbox_list_params.MailboxListParams,
                    ),
                ),
                cast_to=cast(
                    Any, MailboxListResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            f"/mailbox/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnknownResponse,
        )

    def check_availability(
        self,
        *,
        unique_address: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Args:
          uniqueAddress: The unique address of the pipeline

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/mailbox/availability",
            body=maybe_transform(
                {"unique_address": unique_address}, mailbox_check_availability_params.MailboxCheckAvailabilityParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncMailbox(AsyncAPIResource):
    registry: AsyncRegistry
    stream: AsyncStream

    def __init__(self, client: AsyncTecmie) -> None:
        super().__init__(client)
        self.registry = AsyncRegistry(client)
        self.stream = AsyncStream(client)

    async def create(
        self,
        *,
        config: object,
        dotcom: str,
        name: str,
        objective: str,
        unique_address: str,
        workspace_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ReadPipelineDto:
        """
        Args:
          dotcom: The dotcom namespace of the mailbox without the protocol

          name: name of the pipeline

          objective: The objective of the pipeline

          uniqueAddress: The unique address of the pipeline

          workspaceId: Workspace ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/mailbox",
            body=maybe_transform(
                {
                    "config": config,
                    "dotcom": dotcom,
                    "name": name,
                    "objective": objective,
                    "unique_address": unique_address,
                    "workspace_id": workspace_id,
                },
                mailbox_create_params.MailboxCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReadPipelineDto,
        )

    async def retrieve(
        self,
        id: str,
        *,
        cache: int | NotGiven = NOT_GIVEN,
        fields: List[str] | NotGiven = NOT_GIVEN,
        join: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ReadPipelineDto:
        """
        Args:
          cache: Reset cache (if was enabled).
              <a href="https://github.com/nestjsx/crud/wiki/Requests#cache" target="_blank">Docs</a>

          fields: Selects resource fields.
              <a href="https://github.com/nestjsx/crud/wiki/Requests#select" target="_blank">Docs</a>

          join: Adds relational resources.
              <a href="https://github.com/nestjsx/crud/wiki/Requests#join" target="_blank">Docs</a>

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/mailbox/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cache": cache,
                        "fields": fields,
                        "join": join,
                    },
                    mailbox_retrieve_params.MailboxRetrieveParams,
                ),
            ),
            cast_to=ReadPipelineDto,
        )

    async def update(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ReadPipelineDto:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/mailbox/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReadPipelineDto,
        )

    async def list(
        self,
        *,
        cache: int | NotGiven = NOT_GIVEN,
        fields: List[str] | NotGiven = NOT_GIVEN,
        filter: List[str] | NotGiven = NOT_GIVEN,
        join: List[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        or_: List[str] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        s: str | NotGiven = NOT_GIVEN,
        sort: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> MailboxListResponse:
        """
        Args:
          cache: Reset cache (if was enabled).
              <a href="https://github.com/nestjsx/crud/wiki/Requests#cache" target="_blank">Docs</a>

          fields: Selects resource fields.
              <a href="https://github.com/nestjsx/crud/wiki/Requests#select" target="_blank">Docs</a>

          filter: Adds filter condition.
              <a href="https://github.com/nestjsx/crud/wiki/Requests#filter" target="_blank">Docs</a>

          join: Adds relational resources.
              <a href="https://github.com/nestjsx/crud/wiki/Requests#join" target="_blank">Docs</a>

          limit: Limit amount of resources.
              <a href="https://github.com/nestjsx/crud/wiki/Requests#limit" target="_blank">Docs</a>

          offset: Offset amount of resources.
              <a href="https://github.com/nestjsx/crud/wiki/Requests#offset" target="_blank">Docs</a>

          or: Adds OR condition.
              <a href="https://github.com/nestjsx/crud/wiki/Requests#or" target="_blank">Docs</a>

          page: Page portion of resources.
              <a href="https://github.com/nestjsx/crud/wiki/Requests#page" target="_blank">Docs</a>

          s: Adds search condition.
              <a href="https://github.com/nestjsx/crud/wiki/Requests#search" target="_blank">Docs</a>

          sort: Adds sort by field.
              <a href="https://github.com/nestjsx/crud/wiki/Requests#sort" target="_blank">Docs</a>

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            MailboxListResponse,
            await self._get(
                "/mailbox",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {
                            "cache": cache,
                            "fields": fields,
                            "filter": filter,
                            "join": join,
                            "limit": limit,
                            "offset": offset,
                            "or_": or_,
                            "page": page,
                            "s": s,
                            "sort": sort,
                        },
                        mailbox_list_params.MailboxListParams,
                    ),
                ),
                cast_to=cast(
                    Any, MailboxListResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            f"/mailbox/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnknownResponse,
        )

    async def check_availability(
        self,
        *,
        unique_address: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Args:
          uniqueAddress: The unique address of the pipeline

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/mailbox/availability",
            body=maybe_transform(
                {"unique_address": unique_address}, mailbox_check_availability_params.MailboxCheckAvailabilityParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )
