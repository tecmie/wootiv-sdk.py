# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["InvitationAcceptanceUpdateParams"]


class InvitationAcceptanceUpdateParams(TypedDict, total=False):
    passcode: Required[str]
    """Passcode used to activate account"""

    payload: Required[object]
    """
    payload content that will be passed through another module in order to complete
    the activation. This payload will have necessary info required for the target
    module to complete the activation e.g. new password or what ever required info.
    The object not have any strong type defined on purpose because the target
    modules will have different different signatures
    """
