from _typeshed import Incomplete
from octopwn.servers.relay.common.authentication.ntlm.structures.avpair import AVPairs as AVPairs
from octopwn.servers.relay.common.authentication.ntlm.structures.fields import Fields as Fields
from octopwn.servers.relay.common.authentication.ntlm.structures.negotiate_flags import NegotiateFlags as NegotiateFlags
from octopwn.servers.relay.common.authentication.ntlm.structures.version import Version as Version
from octopwn.servers.relay.common.authentication.ntlm.templates.server import NTLMServerTemplates as NTLMServerTemplates

class NTLMChallenge:
    Signature: bytes
    MessageType: int
    TargetNameFields: Incomplete
    NegotiateFlags: Incomplete
    ServerChallenge: Incomplete
    Reserved: Incomplete
    TargetInfoFields: Incomplete
    Version: Incomplete
    Payload: Incomplete
    TargetName: Incomplete
    TargetInfo: Incomplete
    def __init__(self) -> None: ...
    @staticmethod
    def from_bytes(bbuff): ...
    @staticmethod
    def from_buffer(buff): ...
    @staticmethod
    def construct_from_template(templateName, challenge=..., ess: bool = True): ...
    @staticmethod
    def construct(challenge=..., targetName: Incomplete | None = None, targetInfo: Incomplete | None = None, version: Incomplete | None = None, flags: Incomplete | None = None): ...
    def to_bytes(self): ...
    def toBase64(self): ...
