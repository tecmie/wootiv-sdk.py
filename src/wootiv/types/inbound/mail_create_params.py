# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MailCreateParams", "BccFull", "FromFull", "ToFull"]


class MailCreateParams(TypedDict, total=False):
    attachments: Required[Annotated[List[List[object]], PropertyInfo(alias="Attachments")]]

    bcc: Required[Annotated[str, PropertyInfo(alias="Bcc")]]

    bcc_full: Required[Annotated[List[BccFull], PropertyInfo(alias="BccFull")]]

    cc: Required[Annotated[str, PropertyInfo(alias="Cc")]]

    cc_full: Required[Annotated[List[List[object]], PropertyInfo(alias="CcFull")]]

    date: Required[Annotated[str, PropertyInfo(alias="Date")]]

    from_: Required[Annotated[str, PropertyInfo(alias="From")]]

    from_full: Required[Annotated[FromFull, PropertyInfo(alias="FromFull")]]

    from_name: Required[Annotated[str, PropertyInfo(alias="FromName")]]

    headers: Required[Annotated[List[str], PropertyInfo(alias="Headers")]]

    mailbox_hash: Required[Annotated[str, PropertyInfo(alias="MailboxHash")]]

    message_id: Required[Annotated[str, PropertyInfo(alias="MessageID")]]

    message_stream: Required[Annotated[str, PropertyInfo(alias="MessageStream")]]

    original_recipient: Required[Annotated[str, PropertyInfo(alias="OriginalRecipient")]]

    raw_email: Required[Annotated[str, PropertyInfo(alias="RawEmail")]]

    reply_to: Required[Annotated[str, PropertyInfo(alias="ReplyTo")]]

    stripped_text_reply: Required[Annotated[str, PropertyInfo(alias="StrippedTextReply")]]

    subject: Required[Annotated[str, PropertyInfo(alias="Subject")]]

    tag: Required[Annotated[str, PropertyInfo(alias="Tag")]]

    text_body: Required[Annotated[str, PropertyInfo(alias="TextBody")]]

    to: Required[Annotated[str, PropertyInfo(alias="To")]]

    to_full: Required[Annotated[List[ToFull], PropertyInfo(alias="ToFull")]]


class BccFull(TypedDict, total=False):
    email: Required[Annotated[str, PropertyInfo(alias="Email")]]

    mailbox_hash: Required[Annotated[str, PropertyInfo(alias="MailboxHash")]]

    name: Required[Annotated[str, PropertyInfo(alias="Name")]]


class FromFull(TypedDict, total=False):
    email: Required[Annotated[str, PropertyInfo(alias="Email")]]

    mailbox_hash: Required[Annotated[str, PropertyInfo(alias="MailboxHash")]]

    name: Required[Annotated[str, PropertyInfo(alias="Name")]]


class ToFull(TypedDict, total=False):
    email: Required[Annotated[str, PropertyInfo(alias="Email")]]

    mailbox_hash: Required[Annotated[str, PropertyInfo(alias="MailboxHash")]]

    name: Required[Annotated[str, PropertyInfo(alias="Name")]]
