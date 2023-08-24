# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options
from ...types.inbound import mail_create_params

__all__ = ["Mail", "AsyncMail"]


class Mail(SyncAPIResource):
    def create(
        self,
        *,
        attachments: List[List[object]],
        bcc: str,
        bcc_full: List[mail_create_params.BccFull],
        cc: str,
        cc_full: List[List[object]],
        date: str,
        from_: str,
        from_full: mail_create_params.FromFull,
        from_name: str,
        headers: List[str],
        mailbox_hash: str,
        message_id: str,
        message_stream: str,
        original_recipient: str,
        raw_email: str,
        reply_to: str,
        stripped_text_reply: str,
        subject: str,
        tag: str,
        text_body: str,
        to: str,
        to_full: List[mail_create_params.ToFull],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Handle inbound mails

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/inbound/mail",
            body=maybe_transform(
                {
                    "attachments": attachments,
                    "bcc": bcc,
                    "bcc_full": bcc_full,
                    "cc": cc,
                    "cc_full": cc_full,
                    "date": date,
                    "from_": from_,
                    "from_full": from_full,
                    "from_name": from_name,
                    "headers": headers,
                    "mailbox_hash": mailbox_hash,
                    "message_id": message_id,
                    "message_stream": message_stream,
                    "original_recipient": original_recipient,
                    "raw_email": raw_email,
                    "reply_to": reply_to,
                    "stripped_text_reply": stripped_text_reply,
                    "subject": subject,
                    "tag": tag,
                    "text_body": text_body,
                    "to": to,
                    "to_full": to_full,
                },
                mail_create_params.MailCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncMail(AsyncAPIResource):
    async def create(
        self,
        *,
        attachments: List[List[object]],
        bcc: str,
        bcc_full: List[mail_create_params.BccFull],
        cc: str,
        cc_full: List[List[object]],
        date: str,
        from_: str,
        from_full: mail_create_params.FromFull,
        from_name: str,
        headers: List[str],
        mailbox_hash: str,
        message_id: str,
        message_stream: str,
        original_recipient: str,
        raw_email: str,
        reply_to: str,
        stripped_text_reply: str,
        subject: str,
        tag: str,
        text_body: str,
        to: str,
        to_full: List[mail_create_params.ToFull],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Handle inbound mails

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/inbound/mail",
            body=maybe_transform(
                {
                    "attachments": attachments,
                    "bcc": bcc,
                    "bcc_full": bcc_full,
                    "cc": cc,
                    "cc_full": cc_full,
                    "date": date,
                    "from_": from_,
                    "from_full": from_full,
                    "from_name": from_name,
                    "headers": headers,
                    "mailbox_hash": mailbox_hash,
                    "message_id": message_id,
                    "message_stream": message_stream,
                    "original_recipient": original_recipient,
                    "raw_email": raw_email,
                    "reply_to": reply_to,
                    "stripped_text_reply": stripped_text_reply,
                    "subject": subject,
                    "tag": tag,
                    "text_body": text_body,
                    "to": to,
                    "to_full": to_full,
                },
                mail_create_params.MailCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )
