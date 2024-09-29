from _typeshed import Incomplete
from octopwn.servers.relay.common.authentication.ntlm.common.filetime import FILETIME as FILETIME
from octopwn.servers.relay.common.authentication.ntlm.structures.avpair import AVPAIRType as AVPAIRType

NTLMSERVERINFO_TSV_HDR: Incomplete

class NTLMServerInfo:
    domainname: Incomplete
    computername: Incomplete
    dnscomputername: Incomplete
    dnsdomainname: Incomplete
    local_time: Incomplete
    dnsforestname: Incomplete
    os_major_version: Incomplete
    os_minor_version: Incomplete
    os_build: Incomplete
    os_guess: Incomplete
    def __init__(self) -> None: ...
    @staticmethod
    def from_challenge(challenge): ...
    def to_dict(self): ...
    def to_tsv(self, separator: str = '\t'): ...
    def to_json(self): ...
    def to_grep(self): ...
