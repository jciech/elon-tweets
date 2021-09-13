import abc
from google.auth import exceptions as exceptions
from typing import Any

REAUTH_ORIGIN: str

def get_user_password(text): ...

class ReauthChallenge(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def name(self): ...
    @property
    @abc.abstractmethod
    def is_locally_eligible(self): ...
    @abc.abstractmethod
    def obtain_challenge_input(self, metadata): ...

class PasswordChallenge(ReauthChallenge):
    @property
    def name(self): ...
    @property
    def is_locally_eligible(self): ...
    def obtain_challenge_input(self, unused_metadata): ...

class SecurityKeyChallenge(ReauthChallenge):
    @property
    def name(self): ...
    @property
    def is_locally_eligible(self): ...
    def obtain_challenge_input(self, metadata): ...

AVAILABLE_CHALLENGES: Any