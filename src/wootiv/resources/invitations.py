# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Any, List, cast
from typing_extensions import Literal

from ..types import (
    InvitationDto,
    InvitationListResponse,
    invitation_list_params,
    invitation_create_params,
    invitation_retrieve_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven, UnknownResponse
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import make_request_options

__all__ = ["Invitations", "AsyncInvitations"]


class Invitations(SyncAPIResource):
    def create(
        self,
        *,
        category: Literal["invitation", "invite"],
        email: str,
        payload: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> InvitationDto:
        """Create one invitation.

        Category must be `invitation`

        Args:
          category: Category of invitation that refers the following table name: user, org...

          email: Email that the invitation will be sent to

          payload: payload content that will be passed through another module ir order to complete
              the invitation. This payload will have necessary info to target module complete
              the invitation e.g. new password or what ever required info. The object not have
              any strong type defined on purpose because the target moules will have object
              different signatures

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/invitation",
            body=maybe_transform(
                {
                    "category": category,
                    "email": email,
                    "payload": payload,
                },
                invitation_create_params.InvitationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvitationDto,
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
    ) -> InvitationDto:
        """
        Get one invitation by id.

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
            f"/invitation/{id}",
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
                    invitation_retrieve_params.InvitationRetrieveParams,
                ),
            ),
            cast_to=InvitationDto,
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
    ) -> InvitationListResponse:
        """
        Get many invitation using given criteria.

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
            InvitationListResponse,
            self._get(
                "/invitation",
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
                        invitation_list_params.InvitationListParams,
                    ),
                ),
                cast_to=cast(
                    Any, InvitationListResponse
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
        Delete one invitation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            f"/invitation/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnknownResponse,
        )


class AsyncInvitations(AsyncAPIResource):
    async def create(
        self,
        *,
        category: Literal["invitation", "invite"],
        email: str,
        payload: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> InvitationDto:
        """Create one invitation.

        Category must be `invitation`

        Args:
          category: Category of invitation that refers the following table name: user, org...

          email: Email that the invitation will be sent to

          payload: payload content that will be passed through another module ir order to complete
              the invitation. This payload will have necessary info to target module complete
              the invitation e.g. new password or what ever required info. The object not have
              any strong type defined on purpose because the target moules will have object
              different signatures

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/invitation",
            body=maybe_transform(
                {
                    "category": category,
                    "email": email,
                    "payload": payload,
                },
                invitation_create_params.InvitationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvitationDto,
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
    ) -> InvitationDto:
        """
        Get one invitation by id.

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
            f"/invitation/{id}",
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
                    invitation_retrieve_params.InvitationRetrieveParams,
                ),
            ),
            cast_to=InvitationDto,
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
    ) -> InvitationListResponse:
        """
        Get many invitation using given criteria.

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
            InvitationListResponse,
            await self._get(
                "/invitation",
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
                        invitation_list_params.InvitationListParams,
                    ),
                ),
                cast_to=cast(
                    Any, InvitationListResponse
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
        Delete one invitation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            f"/invitation/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnknownResponse,
        )
