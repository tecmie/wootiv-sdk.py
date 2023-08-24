# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ..types import (
    invitation_acceptance_update_params,
    invitation_acceptance_retrieve_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import make_request_options

__all__ = ["InvitationAcceptance", "AsyncInvitationAcceptance"]


class InvitationAcceptance(SyncAPIResource):
    def retrieve(
        self,
        code: str,
        *,
        passcode: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Check if passcode is valid.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/invitation_acceptance/{code}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"passcode": passcode}, invitation_acceptance_retrieve_params.InvitationAcceptanceRetrieveParams
                ),
            ),
            cast_to=NoneType,
        )

    def update(
        self,
        code: str,
        *,
        passcode: str,
        payload: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Accept one invitation by code, passcode and payload.

        Args:
          passcode: Passcode used to activate account

          payload: payload content that will be passed through another module in order to complete
              the activation. This payload will have necessary info required for the target
              module to complete the activation e.g. new password or what ever required info.
              The object not have any strong type defined on purpose because the target
              modules will have different different signatures

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            f"/invitation_acceptance/{code}",
            body=maybe_transform(
                {
                    "passcode": passcode,
                    "payload": payload,
                },
                invitation_acceptance_update_params.InvitationAcceptanceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncInvitationAcceptance(AsyncAPIResource):
    async def retrieve(
        self,
        code: str,
        *,
        passcode: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Check if passcode is valid.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/invitation_acceptance/{code}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"passcode": passcode}, invitation_acceptance_retrieve_params.InvitationAcceptanceRetrieveParams
                ),
            ),
            cast_to=NoneType,
        )

    async def update(
        self,
        code: str,
        *,
        passcode: str,
        payload: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Accept one invitation by code, passcode and payload.

        Args:
          passcode: Passcode used to activate account

          payload: payload content that will be passed through another module in order to complete
              the activation. This payload will have necessary info required for the target
              module to complete the activation e.g. new password or what ever required info.
              The object not have any strong type defined on purpose because the target
              modules will have different different signatures

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            f"/invitation_acceptance/{code}",
            body=maybe_transform(
                {
                    "passcode": passcode,
                    "payload": payload,
                },
                invitation_acceptance_update_params.InvitationAcceptanceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )
