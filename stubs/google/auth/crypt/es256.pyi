from google.auth.crypt import base as base
from typing import Any

class ES256Verifier(base.Verifier):
    def __init__(self, public_key) -> None: ...
    def verify(self, message, signature): ...
    @classmethod
    def from_string(cls, public_key): ...

class ES256Signer(base.Signer, base.FromServiceAccountMixin):
    def __init__(self, private_key, key_id: Any | None = ...) -> None: ...
    @property
    def key_id(self): ...
    def sign(self, message): ...
    @classmethod
    def from_string(cls, key, key_id: Any | None = ...): ...
