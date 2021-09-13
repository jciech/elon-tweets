from google.auth import _credentials_async as credentials_async
from google.oauth2 import service_account as service_account
from typing import Any

class Credentials(service_account.Credentials, credentials_async.Scoped, credentials_async.Credentials):
    token: Any
    expiry: Any
    async def refresh(self, request) -> None: ...

class IDTokenCredentials(service_account.IDTokenCredentials, credentials_async.Signing, credentials_async.Credentials):
    token: Any
    expiry: Any
    async def refresh(self, request) -> None: ...
