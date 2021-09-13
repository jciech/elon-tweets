from google.auth import environment_vars as environment_vars, exceptions as exceptions
from typing import Any, Optional

class AuthMetadataPlugin:
    def __init__(self, credentials: Any, request: Any) -> None: ...
    def __call__(self, context: Any, callback: Any) -> None: ...

def secure_authorized_channel(
    credentials: Any,
    request: Any,
    target: Any,
    ssl_credentials: Optional[Any] = ...,
    client_cert_callback: Optional[Any] = ...,
    **kwargs: Any
): ...

class SslCredentials:
    def __init__(self) -> None: ...
    @property
    def ssl_credentials(self): ...
    @property
    def is_mtls(self): ...
