# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

from .token import Token, AsyncToken
from ...types import (
    AuthLoginResponse,
    AuthSignupResponse,
    AuthVerifyBillingResponse,
    auth_login_params,
    auth_signup_params,
    auth_verify_billing_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from .recovery import Recovery, AsyncRecovery
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options

if TYPE_CHECKING:
    from ..._client import Tecmie, AsyncTecmie

__all__ = ["Auth", "AsyncAuth"]


class Auth(SyncAPIResource):
    token: Token
    recovery: Recovery

    def __init__(self, client: Tecmie) -> None:
        super().__init__(client)
        self.token = Token(client)
        self.recovery = Recovery(client)

    def login(
        self,
        *,
        password: str,
        username: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AuthLoginResponse:
        """
        Args:
          password: Password

          username: Username

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/auth/login",
            body=maybe_transform(
                {
                    "password": password,
                    "username": username,
                },
                auth_login_params.AuthLoginParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthLoginResponse,
        )

    def signup(
        self,
        *,
        email: str,
        password: str,
        plan: str,
        first_name: str | NotGiven = NOT_GIVEN,
        last_name: str | NotGiven = NOT_GIVEN,
        phone_number: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AuthSignupResponse:
        """
        Args:
          email: Email

          password: Password

          plan: Trial plan

          firstName: First name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/auth/signup",
            body=maybe_transform(
                {
                    "email": email,
                    "password": password,
                    "plan": plan,
                    "first_name": first_name,
                    "last_name": last_name,
                    "phone_number": phone_number,
                },
                auth_signup_params.AuthSignupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthSignupResponse,
        )

    def verify_billing(
        self,
        *,
        sub: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AuthVerifyBillingResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/auth/verify_billing",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"sub": sub}, auth_verify_billing_params.AuthVerifyBillingParams),
            ),
            cast_to=AuthVerifyBillingResponse,
        )


class AsyncAuth(AsyncAPIResource):
    token: AsyncToken
    recovery: AsyncRecovery

    def __init__(self, client: AsyncTecmie) -> None:
        super().__init__(client)
        self.token = AsyncToken(client)
        self.recovery = AsyncRecovery(client)

    async def login(
        self,
        *,
        password: str,
        username: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AuthLoginResponse:
        """
        Args:
          password: Password

          username: Username

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/auth/login",
            body=maybe_transform(
                {
                    "password": password,
                    "username": username,
                },
                auth_login_params.AuthLoginParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthLoginResponse,
        )

    async def signup(
        self,
        *,
        email: str,
        password: str,
        plan: str,
        first_name: str | NotGiven = NOT_GIVEN,
        last_name: str | NotGiven = NOT_GIVEN,
        phone_number: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AuthSignupResponse:
        """
        Args:
          email: Email

          password: Password

          plan: Trial plan

          firstName: First name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/auth/signup",
            body=maybe_transform(
                {
                    "email": email,
                    "password": password,
                    "plan": plan,
                    "first_name": first_name,
                    "last_name": last_name,
                    "phone_number": phone_number,
                },
                auth_signup_params.AuthSignupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthSignupResponse,
        )

    async def verify_billing(
        self,
        *,
        sub: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AuthVerifyBillingResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/auth/verify_billing",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"sub": sub}, auth_verify_billing_params.AuthVerifyBillingParams),
            ),
            cast_to=AuthVerifyBillingResponse,
        )
