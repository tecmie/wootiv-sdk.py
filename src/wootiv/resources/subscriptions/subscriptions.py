# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, List, Union
from datetime import datetime
from typing_extensions import Literal

from .change import Change, AsyncChange
from ...types import (
    SubscriptionDto,
    shared_params,
    subscription_create_params,
    subscription_update_params,
    subscription_retrieve_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options

if TYPE_CHECKING:
    from ..._client import Wootiv, AsyncWootiv

__all__ = ["Subscriptions", "AsyncSubscriptions"]


class Subscriptions(SyncAPIResource):
    change: Change

    def __init__(self, client: Wootiv) -> None:
        super().__init__(client)
        self.change = Change(client)

    def create(
        self,
        *,
        end_date: Union[str, datetime],
        plan_name: Literal["free", "personal_pro", "business_pro", "enterprise"],
        start_date: Union[str, datetime],
        status: Literal["active", "inactive", "trial", "canceled", "expired"],
        workspace_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SubscriptionDto:
        """
        Create one subscription.

        Args:
          endDate: Subscription end date

          planName: Subscription Plan Name

          startDate: Subscription start date

          status: Subscription status

          workspaceId: Unique Workspace ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/subscription",
            body=maybe_transform(
                {
                    "end_date": end_date,
                    "plan_name": plan_name,
                    "start_date": start_date,
                    "status": status,
                    "workspace_id": workspace_id,
                },
                subscription_create_params.SubscriptionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionDto,
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
    ) -> SubscriptionDto:
        """
        Get one subscription by id.

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
            f"/subscription/{id}",
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
                    subscription_retrieve_params.SubscriptionRetrieveParams,
                ),
            ),
            cast_to=SubscriptionDto,
        )

    def update(
        self,
        path_id: str,
        *,
        body_id: str | NotGiven = NOT_GIVEN,
        audit: shared_params.AuditDto | NotGiven = NOT_GIVEN,
        end_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        history: List[List[object]] | NotGiven = NOT_GIVEN,
        plan_name: Literal["free", "personal_pro", "business_pro", "enterprise"] | NotGiven = NOT_GIVEN,
        start_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        status: Literal["active", "inactive", "trial", "canceled", "expired"] | NotGiven = NOT_GIVEN,
        workspace: object | NotGiven = NOT_GIVEN,
        workspace_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SubscriptionDto:
        """
        Update one subscription.

        Args:
          id: Subscription ID

          audit: Audit data

          endDate: Subscription end date

          planName: Subscription Plan Name

          startDate: Subscription start date

          status: Subscription status

          workspace: Workspace Associated with this subscription

          workspaceId: Unique Workspace ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/subscription/{path_id}",
            body=maybe_transform(
                {
                    "id": body_id,
                    "audit": audit,
                    "end_date": end_date,
                    "history": history,
                    "plan_name": plan_name,
                    "start_date": start_date,
                    "status": status,
                    "workspace": workspace,
                    "workspace_id": workspace_id,
                },
                subscription_update_params.SubscriptionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionDto,
        )


class AsyncSubscriptions(AsyncAPIResource):
    change: AsyncChange

    def __init__(self, client: AsyncWootiv) -> None:
        super().__init__(client)
        self.change = AsyncChange(client)

    async def create(
        self,
        *,
        end_date: Union[str, datetime],
        plan_name: Literal["free", "personal_pro", "business_pro", "enterprise"],
        start_date: Union[str, datetime],
        status: Literal["active", "inactive", "trial", "canceled", "expired"],
        workspace_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SubscriptionDto:
        """
        Create one subscription.

        Args:
          endDate: Subscription end date

          planName: Subscription Plan Name

          startDate: Subscription start date

          status: Subscription status

          workspaceId: Unique Workspace ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/subscription",
            body=maybe_transform(
                {
                    "end_date": end_date,
                    "plan_name": plan_name,
                    "start_date": start_date,
                    "status": status,
                    "workspace_id": workspace_id,
                },
                subscription_create_params.SubscriptionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionDto,
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
    ) -> SubscriptionDto:
        """
        Get one subscription by id.

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
            f"/subscription/{id}",
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
                    subscription_retrieve_params.SubscriptionRetrieveParams,
                ),
            ),
            cast_to=SubscriptionDto,
        )

    async def update(
        self,
        path_id: str,
        *,
        body_id: str | NotGiven = NOT_GIVEN,
        audit: shared_params.AuditDto | NotGiven = NOT_GIVEN,
        end_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        history: List[List[object]] | NotGiven = NOT_GIVEN,
        plan_name: Literal["free", "personal_pro", "business_pro", "enterprise"] | NotGiven = NOT_GIVEN,
        start_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        status: Literal["active", "inactive", "trial", "canceled", "expired"] | NotGiven = NOT_GIVEN,
        workspace: object | NotGiven = NOT_GIVEN,
        workspace_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SubscriptionDto:
        """
        Update one subscription.

        Args:
          id: Subscription ID

          audit: Audit data

          endDate: Subscription end date

          planName: Subscription Plan Name

          startDate: Subscription start date

          status: Subscription status

          workspace: Workspace Associated with this subscription

          workspaceId: Unique Workspace ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/subscription/{path_id}",
            body=maybe_transform(
                {
                    "id": body_id,
                    "audit": audit,
                    "end_date": end_date,
                    "history": history,
                    "plan_name": plan_name,
                    "start_date": start_date,
                    "status": status,
                    "workspace": workspace,
                    "workspace_id": workspace_id,
                },
                subscription_update_params.SubscriptionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionDto,
        )
