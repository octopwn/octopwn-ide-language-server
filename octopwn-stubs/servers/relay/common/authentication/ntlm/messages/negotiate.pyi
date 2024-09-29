from _typeshed import Incomplete
from octopwn.servers.relay.common.authentication.ntlm.structures.fields import Fields as Fields
from octopwn.servers.relay.common.authentication.ntlm.structures.negotiate_flags import NegotiateFlags as NegotiateFlags
from octopwn.servers.relay.common.authentication.ntlm.structures.version import Version as Version

class NTLMNegotiate:
    Signature: bytes
    MessageType: int
    NegotiateFlags: Incomplete
    DomainNameFields: Incomplete
    WorkstationFields: Incomplete
    Version: Incomplete
    Payload: Incomplete
    Domain: Incomplete
    Workstation: Incomplete
    def __init__(self) -> None: ...
    @staticmethod
    def from_bytes(bbuff): ...
    @staticmethod
    def from_buffer(buff): ...
    @staticmethod
    def construct(flags, domainname: Incomplete | None = None, workstationname: Incomplete | None = None, version: Incomplete | None = None): ...
    def to_bytes(self): ...
