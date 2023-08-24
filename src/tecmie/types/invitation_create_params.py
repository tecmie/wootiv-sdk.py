# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["InvitationCreateParams"]


class InvitationCreateParams(TypedDict, total=False):
    category: Required[Literal["invitation", "invite"]]
    """Category of invitation that refers the following table name: user, org..."""

    email: Required[str]
    """Email that the invitation will be sent to"""

    payload: Required[object]
    """
    payload content that will be passed through another module ir order to complete
    the invitation. This payload will have necessary info to target module complete
    the invitation e.g. new password or what ever required info. The object not have
    any strong type defined on purpose because the target moules will have object
    different signatures
    """
