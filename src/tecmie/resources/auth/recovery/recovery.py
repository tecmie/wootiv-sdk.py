# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

from .login import Login, AsyncLogin
from .passcode import Passcode, AsyncPasscode
from .password import Password, AsyncPassword
from ...._resource import SyncAPIResource, AsyncAPIResource

if TYPE_CHECKING:
    from ...._client import Tecmie, AsyncTecmie

__all__ = ["Recovery", "AsyncRecovery"]


class Recovery(SyncAPIResource):
    login: Login
    password: Password
    passcode: Passcode

    def __init__(self, client: Tecmie) -> None:
        super().__init__(client)
        self.login = Login(client)
        self.password = Password(client)
        self.passcode = Passcode(client)


class AsyncRecovery(AsyncAPIResource):
    login: AsyncLogin
    password: AsyncPassword
    passcode: AsyncPasscode

    def __init__(self, client: AsyncTecmie) -> None:
        super().__init__(client)
        self.login = AsyncLogin(client)
        self.password = AsyncPassword(client)
        self.passcode = AsyncPasscode(client)
