from _typeshed import Incomplete

class NTLMClientSettings:
    signdisable: Incomplete
    dropmic: Incomplete
    dropmic2: Incomplete
    modify_negotiate_cb: Incomplete
    modify_challenge_cb: Incomplete
    modify_authenticate_cb: Incomplete
    def __init__(self, signdisable: bool = False, dropmic: bool = False, dropmic2: bool = False) -> None: ...
    def to_dict(self): ...
    @staticmethod
    def from_keyword(keyword): ...
    @staticmethod
    def from_dict(d): ...
    @staticmethod
    def from_json(x): ...
    @staticmethod
    def from_toml(x): ...
    def to_toml(self): ...
    def to_json(self): ...
