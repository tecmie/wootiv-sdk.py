# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

from ...types import AwsS3GetSignedURLResponse, aw_create_signed_put_url_params
from .buckets import Buckets, AsyncBuckets
from .objects import Objects, AsyncObjects
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options

if TYPE_CHECKING:
    from ..._client import Tecmie, AsyncTecmie

__all__ = ["Aws", "AsyncAws"]


class Aws(SyncAPIResource):
    buckets: Buckets
    objects: Objects

    def __init__(self, client: Tecmie) -> None:
        super().__init__(client)
        self.buckets = Buckets(client)
        self.objects = Objects(client)

    def create_signed_put_url(
        self,
        *,
        filename: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AwsS3GetSignedURLResponse:
        """
        Args:
          filename: The name of the file we are creating namespace for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/aws/get-signed-put-url",
            body=maybe_transform({"filename": filename}, aw_create_signed_put_url_params.AwCreateSignedPutURLParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AwsS3GetSignedURLResponse,
        )


class AsyncAws(AsyncAPIResource):
    buckets: AsyncBuckets
    objects: AsyncObjects

    def __init__(self, client: AsyncTecmie) -> None:
        super().__init__(client)
        self.buckets = AsyncBuckets(client)
        self.objects = AsyncObjects(client)

    async def create_signed_put_url(
        self,
        *,
        filename: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AwsS3GetSignedURLResponse:
        """
        Args:
          filename: The name of the file we are creating namespace for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/aws/get-signed-put-url",
            body=maybe_transform({"filename": filename}, aw_create_signed_put_url_params.AwCreateSignedPutURLParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AwsS3GetSignedURLResponse,
        )
