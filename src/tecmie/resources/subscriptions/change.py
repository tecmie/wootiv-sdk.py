# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal

from ...types import SubscriptionDto, shared_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options
from ...types.subscriptions import change_update_params

__all__ = ["Change", "AsyncChange"]


class Change(SyncAPIResource):
    def update(
        self,
        *,
        path_id: str,
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
        Change Subscription

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
            f"/subscription/change",
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
                change_update_params.ChangeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionDto,
        )


class AsyncChange(AsyncAPIResource):
    async def update(
        self,
        *,
        path_id: str,
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
        Change Subscription

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
            f"/subscription/change",
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
                change_update_params.ChangeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionDto,
        )
