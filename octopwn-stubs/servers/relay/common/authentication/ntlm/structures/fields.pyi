from _typeshed import Incomplete

class Fields:
    length: Incomplete
    maxLength: Incomplete
    offset: Incomplete
    def __init__(self, length, offset, maxLength: Incomplete | None = None) -> None: ...
    @staticmethod
    def from_bytes(bbuff): ...
    @staticmethod
    def from_buffer(buff): ...
    def to_bytes(self): ...
