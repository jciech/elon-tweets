from google.auth import exceptions as exceptions
from google.oauth2 import challenges as challenges
from typing import Any

RUN_CHALLENGE_RETRY_LIMIT: int

def is_interactive(): ...
def get_rapt_token(request, client_id, client_secret, refresh_token, token_uri, scopes: Any | None = ...): ...
def refresh_grant(request, token_uri, refresh_token, client_id, client_secret, scopes: Any | None = ..., rapt_token: Any | None = ...): ...
