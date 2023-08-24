# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options
from ...types.role_assignments import BulkCreateResponse, bulk_create_params

__all__ = ["Bulk", "AsyncBulk"]


class Bulk(SyncAPIResource):
    def create(
        self,
        assignment: str,
        *,
        bulk: List[bulk_create_params.Bulk],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> BulkCreateResponse:
        """
        Args:
          bulk: Array of Roles Assignments to create

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/role-assignment/{assignment}/bulk",
            body=maybe_transform({"bulk": bulk}, bulk_create_params.BulkCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkCreateResponse,
        )


class AsyncBulk(AsyncAPIResource):
    async def create(
        self,
        assignment: str,
        *,
        bulk: List[bulk_create_params.Bulk],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> BulkCreateResponse:
        """
        Args:
          bulk: Array of Roles Assignments to create

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/role-assignment/{assignment}/bulk",
            body=maybe_transform({"bulk": bulk}, bulk_create_params.BulkCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkCreateResponse,
        )
