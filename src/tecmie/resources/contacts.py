# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Any, List, cast

from ..types import (
    ReadContactDto,
    ContactListResponse,
    contact_list_params,
    contact_create_params,
    contact_update_params,
    contact_retrieve_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven, UnknownResponse
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import make_request_options

__all__ = ["Contacts", "AsyncContacts"]


class Contacts(SyncAPIResource):
    def create(
        self,
        *,
        contact_group_id: str,
        email: str,
        first_name: str,
        last_name: str,
        metadata: object,
        phone_number: str,
        workspace_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ReadContactDto:
        """
        Args:
          contactGroupId: The id for the contact group

          email: The email for the contact

          firstName: The name for the contact

          lastName: The lastname for the contact

          metadata: The metadata for the contact

          phoneNumber: The phone for the contact

          workspaceId: The ID of thw workspace the contact contact belongs to

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/contacts",
            body=maybe_transform(
                {
                    "contact_group_id": contact_group_id,
                    "email": email,
                    "first_name": first_name,
                    "last_name": last_name,
                    "metadata": metadata,
                    "phone_number": phone_number,
                    "workspace_id": workspace_id,
                },
                contact_create_params.ContactCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReadContactDto,
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
    ) -> ReadContactDto:
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
            f"/contacts/{id}",
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
                    contact_retrieve_params.ContactRetrieveParams,
                ),
            ),
            cast_to=ReadContactDto,
        )

    def update(
        self,
        id: str,
        *,
        contact_group_id: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        first_name: str | NotGiven = NOT_GIVEN,
        last_name: str | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        phone_number: str | NotGiven = NOT_GIVEN,
        workspace_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ReadContactDto:
        """
        Args:
          contactGroupId: The id for the contact group

          email: The email for the contact

          firstName: The name for the contact

          lastName: The lastname for the contact

          metadata: The metadata for the contact

          phoneNumber: The phone for the contact

          workspaceId: The ID of thw workspace the contact contact belongs to

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/contacts/{id}",
            body=maybe_transform(
                {
                    "contact_group_id": contact_group_id,
                    "email": email,
                    "first_name": first_name,
                    "last_name": last_name,
                    "metadata": metadata,
                    "phone_number": phone_number,
                    "workspace_id": workspace_id,
                },
                contact_update_params.ContactUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReadContactDto,
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
    ) -> ContactListResponse:
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
            ContactListResponse,
            self._get(
                "/contacts",
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
                        contact_list_params.ContactListParams,
                    ),
                ),
                cast_to=cast(
                    Any, ContactListResponse
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
            f"/contacts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnknownResponse,
        )


class AsyncContacts(AsyncAPIResource):
    async def create(
        self,
        *,
        contact_group_id: str,
        email: str,
        first_name: str,
        last_name: str,
        metadata: object,
        phone_number: str,
        workspace_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ReadContactDto:
        """
        Args:
          contactGroupId: The id for the contact group

          email: The email for the contact

          firstName: The name for the contact

          lastName: The lastname for the contact

          metadata: The metadata for the contact

          phoneNumber: The phone for the contact

          workspaceId: The ID of thw workspace the contact contact belongs to

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/contacts",
            body=maybe_transform(
                {
                    "contact_group_id": contact_group_id,
                    "email": email,
                    "first_name": first_name,
                    "last_name": last_name,
                    "metadata": metadata,
                    "phone_number": phone_number,
                    "workspace_id": workspace_id,
                },
                contact_create_params.ContactCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReadContactDto,
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
    ) -> ReadContactDto:
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
            f"/contacts/{id}",
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
                    contact_retrieve_params.ContactRetrieveParams,
                ),
            ),
            cast_to=ReadContactDto,
        )

    async def update(
        self,
        id: str,
        *,
        contact_group_id: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        first_name: str | NotGiven = NOT_GIVEN,
        last_name: str | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        phone_number: str | NotGiven = NOT_GIVEN,
        workspace_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ReadContactDto:
        """
        Args:
          contactGroupId: The id for the contact group

          email: The email for the contact

          firstName: The name for the contact

          lastName: The lastname for the contact

          metadata: The metadata for the contact

          phoneNumber: The phone for the contact

          workspaceId: The ID of thw workspace the contact contact belongs to

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/contacts/{id}",
            body=maybe_transform(
                {
                    "contact_group_id": contact_group_id,
                    "email": email,
                    "first_name": first_name,
                    "last_name": last_name,
                    "metadata": metadata,
                    "phone_number": phone_number,
                    "workspace_id": workspace_id,
                },
                contact_update_params.ContactUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReadContactDto,
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
    ) -> ContactListResponse:
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
            ContactListResponse,
            await self._get(
                "/contacts",
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
                        contact_list_params.ContactListParams,
                    ),
                ),
                cast_to=cast(
                    Any, ContactListResponse
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
            f"/contacts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnknownResponse,
        )
