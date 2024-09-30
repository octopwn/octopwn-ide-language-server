from octopwn.servers.relay.common.authentication.ntlm.structures.challenge_response import *
from _typeshed import Incomplete
from octopwn.servers.relay.common.authentication.ntlm.structures.avpair import AVPAIRType as AVPAIRType, MsvAvFlags as MsvAvFlags
from octopwn.servers.relay.common.authentication.ntlm.structures.fields import Fields as Fields
from octopwn.servers.relay.common.authentication.ntlm.structures.negotiate_flags import NegotiateFlags as NegotiateFlags
from octopwn.servers.relay.common.authentication.ntlm.structures.version import Version as Version

class NTLMAuthenticate:
    Signature: bytes
    MessageType: int
    LmChallengeResponseFields: Incomplete
    NtChallengeResponseFields: Incomplete
    DomainNameFields: Incomplete
    UserNameFields: Incomplete
    WorkstationFields: Incomplete
    EncryptedRandomSessionKeyFields: Incomplete
    NegotiateFlags: Incomplete
    Version: Incomplete
    MIC: Incomplete
    Payload: Incomplete
    LMChallenge: Incomplete
    NTChallenge: Incomplete
    DomainName: Incomplete
    UserName: Incomplete
    Workstation: Incomplete
    EncryptedRandomSession: Incomplete
    def __init__(self, _use_NTLMv2: bool = True) -> None: ...
    @staticmethod
    def construct(flags, domainname: Incomplete | None = None, workstationname: Incomplete | None = None, username: Incomplete | None = None, encrypted_session: Incomplete | None = None, lm_response: Incomplete | None = None, nt_response: Incomplete | None = None, version: Incomplete | None = None, mic=...): ...
    def to_bytes(self): ...
    def to_bytes_full(self): ...
    @staticmethod
    def from_bytes(bbuff, _use_NTLMv2: bool = True): ...
    @staticmethod
    def from_buffer(buff: bytes, _use_NTLMv2: bool = True): ...
