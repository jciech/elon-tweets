from google.auth import exceptions as exceptions
from google.oauth2 import credentials as oauth2_credentials
from typing import Any

class Credentials(oauth2_credentials.Credentials):
    token: Any
    expiry: Any
    async def refresh(self, request) -> None: ...

class UserAccessTokenCredentials(oauth2_credentials.UserAccessTokenCredentials): ...
