from google.auth import environment_vars as environment_vars, exceptions as exceptions
from typing import Any

def load_credentials_from_file(filename, scopes: Any | None = ..., quota_project_id: Any | None = ...): ...
def default_async(scopes: Any | None = ..., request: Any | None = ..., quota_project_id: Any | None = ...): ...