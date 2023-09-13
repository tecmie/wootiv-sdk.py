# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Any, List, cast

from ..types import (
    RoleDto,
    RoleListResponse,
    RoleBulkCreateResponse,
    role_list_params,
    role_create_params,
    role_update_params,
    role_retrieve_params,
    role_bulk_create_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven, UnknownResponse
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import make_request_options

__all__ = ["Roles", "AsyncRoles"]


class Roles(SyncAPIResource):
    def create(
        self,
        *,
        description: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> RoleDto:
        """
        Args:
          description: Description of the role

          name: Name of the role

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/role",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                role_create_params.RoleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoleDto,
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
    ) -> RoleDto:
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
            f"/role/{id}",
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
                    role_retrieve_params.RoleRetrieveParams,
                ),
            ),
            cast_to=RoleDto,
        )

    def update(
        self,
        id: str,
        *,
        description: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> RoleDto:
        """
        Args:
          description: Description of the role

          name: Name of the role

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/role/{id}",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                role_update_params.RoleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoleDto,
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
    ) -> RoleListResponse:
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
            RoleListResponse,
            self._get(
                "/role",
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
                        role_list_params.RoleListParams,
                    ),
                ),
                cast_to=cast(Any, RoleListResponse),  # Union types cannot be passed in as arguments in the type system
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
            f"/role/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnknownResponse,
        )

    def bulk_create(
        self,
        *,
        bulk: List[role_bulk_create_params.Bulk],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> RoleBulkCreateResponse:
        """
        Args:
          bulk: Array of Roles to create

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/role/bulk",
            body=maybe_transform({"bulk": bulk}, role_bulk_create_params.RoleBulkCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoleBulkCreateResponse,
        )


class AsyncRoles(AsyncAPIResource):
    async def create(
        self,
        *,
        description: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> RoleDto:
        """
        Args:
          description: Description of the role

          name: Name of the role

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/role",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                role_create_params.RoleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoleDto,
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
    ) -> RoleDto:
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
            f"/role/{id}",
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
                    role_retrieve_params.RoleRetrieveParams,
                ),
            ),
            cast_to=RoleDto,
        )

    async def update(
        self,
        id: str,
        *,
        description: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> RoleDto:
        """
        Args:
          description: Description of the role

          name: Name of the role

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/role/{id}",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                role_update_params.RoleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoleDto,
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
    ) -> RoleListResponse:
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
            RoleListResponse,
            await self._get(
                "/role",
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
                        role_list_params.RoleListParams,
                    ),
                ),
                cast_to=cast(Any, RoleListResponse),  # Union types cannot be passed in as arguments in the type system
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
            f"/role/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnknownResponse,
        )

    async def bulk_create(
        self,
        *,
        bulk: List[role_bulk_create_params.Bulk],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> RoleBulkCreateResponse:
        """
        Args:
          bulk: Array of Roles to create

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/role/bulk",
            body=maybe_transform({"bulk": bulk}, role_bulk_create_params.RoleBulkCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoleBulkCreateResponse,
        )
