# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List

from ..types import (
    WorkspaceDto,
    wspace_create_params,
    wspace_update_params,
    wspace_retrieve_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import make_request_options

__all__ = ["Wspaces", "AsyncWspaces"]


class Wspaces(SyncAPIResource):
    def create(
        self,
        *,
        name: str,
        owner_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> WorkspaceDto:
        """
        Create new workspace.

        Args:
          name: The name of the workspace

          ownerId: The unique identifier of the workspace owner

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/wspace",
            body=maybe_transform(
                {
                    "name": name,
                    "owner_id": owner_id,
                },
                wspace_create_params.WspaceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkspaceDto,
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
    ) -> WorkspaceDto:
        """
        Get User Workspace by slug

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
            f"/wspace/{id}",
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
                    wspace_retrieve_params.WspaceRetrieveParams,
                ),
            ),
            cast_to=WorkspaceDto,
        )

    def update(
        self,
        path_id: str,
        *,
        body_id: str | NotGiven = NOT_GIVEN,
        audit: object | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        owner_id: str | NotGiven = NOT_GIVEN,
        slug: str | NotGiven = NOT_GIVEN,
        subscription: object | NotGiven = NOT_GIVEN,
        subscription_id: str | NotGiven = NOT_GIVEN,
        workspace_members: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> WorkspaceDto:
        """
        Update workspace.

        Args:
          id: The unique identifier of the workspace

          audit: Audit information including createdAt and updatedAt timestamps

          name: The name of the workspace

          ownerId: The unique identifier of the workspace owner

          slug: The URL Identifier for this workspace

          subscription: The subscription associated with the workspace

          subscriptionId: The subscription attached to this workspace

          workspaceMembers: The members associated with the workspace

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/wspace/{path_id}",
            body=maybe_transform(
                {
                    "id": body_id,
                    "audit": audit,
                    "name": name,
                    "owner_id": owner_id,
                    "slug": slug,
                    "subscription": subscription,
                    "subscription_id": subscription_id,
                    "workspace_members": workspace_members,
                },
                wspace_update_params.WspaceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkspaceDto,
        )


class AsyncWspaces(AsyncAPIResource):
    async def create(
        self,
        *,
        name: str,
        owner_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> WorkspaceDto:
        """
        Create new workspace.

        Args:
          name: The name of the workspace

          ownerId: The unique identifier of the workspace owner

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/wspace",
            body=maybe_transform(
                {
                    "name": name,
                    "owner_id": owner_id,
                },
                wspace_create_params.WspaceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkspaceDto,
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
    ) -> WorkspaceDto:
        """
        Get User Workspace by slug

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
            f"/wspace/{id}",
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
                    wspace_retrieve_params.WspaceRetrieveParams,
                ),
            ),
            cast_to=WorkspaceDto,
        )

    async def update(
        self,
        path_id: str,
        *,
        body_id: str | NotGiven = NOT_GIVEN,
        audit: object | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        owner_id: str | NotGiven = NOT_GIVEN,
        slug: str | NotGiven = NOT_GIVEN,
        subscription: object | NotGiven = NOT_GIVEN,
        subscription_id: str | NotGiven = NOT_GIVEN,
        workspace_members: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> WorkspaceDto:
        """
        Update workspace.

        Args:
          id: The unique identifier of the workspace

          audit: Audit information including createdAt and updatedAt timestamps

          name: The name of the workspace

          ownerId: The unique identifier of the workspace owner

          slug: The URL Identifier for this workspace

          subscription: The subscription associated with the workspace

          subscriptionId: The subscription attached to this workspace

          workspaceMembers: The members associated with the workspace

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/wspace/{path_id}",
            body=maybe_transform(
                {
                    "id": body_id,
                    "audit": audit,
                    "name": name,
                    "owner_id": owner_id,
                    "slug": slug,
                    "subscription": subscription,
                    "subscription_id": subscription_id,
                    "workspace_members": workspace_members,
                },
                wspace_update_params.WspaceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkspaceDto,
        )
