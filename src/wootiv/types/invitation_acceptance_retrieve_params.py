# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["InvitationAcceptanceRetrieveParams"]


class InvitationAcceptanceRetrieveParams(TypedDict, total=False):
    passcode: Required[str]
