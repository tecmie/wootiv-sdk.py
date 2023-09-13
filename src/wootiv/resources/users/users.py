# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Any, List, cast

from ...types import UserDto, UserListResponse, user_list_params, user_retrieve_params
from .recover import Recover, AsyncRecover
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options

if TYPE_CHECKING:
    from ..._client import Wootiv, AsyncWootiv

__all__ = ["Users", "AsyncUsers"]


class Users(SyncAPIResource):
    recover: Recover

    def __init__(self, client: Wootiv) -> None:
        super().__init__(client)
        self.recover = Recover(client)

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
    ) -> UserDto:
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
            f"/user/{id}",
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
                    user_retrieve_params.UserRetrieveParams,
                ),
            ),
            cast_to=UserDto,
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
    ) -> UserListResponse:
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
            UserListResponse,
            self._get(
                "/user",
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
                        user_list_params.UserListParams,
                    ),
                ),
                cast_to=cast(Any, UserListResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncUsers(AsyncAPIResource):
    recover: AsyncRecover

    def __init__(self, client: AsyncWootiv) -> None:
        super().__init__(client)
        self.recover = AsyncRecover(client)

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
    ) -> UserDto:
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
            f"/user/{id}",
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
                    user_retrieve_params.UserRetrieveParams,
                ),
            ),
            cast_to=UserDto,
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
    ) -> UserListResponse:
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
            UserListResponse,
            await self._get(
                "/user",
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
                        user_list_params.UserListParams,
                    ),
                ),
                cast_to=cast(Any, UserListResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )
