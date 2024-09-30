from unicrypto.hashlib import *
from unicrypto.hmac import *
from octopwn.servers.relay.common.authentication.ntlm.structures.challenge_response import *
from _typeshed import Incomplete
from octopwn.servers.relay.common.authentication.ntlm.structures.negotiate_flags import NegotiateFlags as NegotiateFlags

class Credential:
    credtype: Incomplete
    username: Incomplete
    domain: Incomplete
    fullhash: Incomplete
    def __init__(self, credtype, username: Incomplete | None = None, domain: Incomplete | None = None, fullhash: Incomplete | None = None) -> None: ...

class NTLMCredentials:
    @staticmethod
    def construct(ntlmNegotiate, ntlmChallenge, ntlmAuthenticate): ...

class netlm:
    username: Incomplete
    domain: Incomplete
    ServerChallenge: Incomplete
    ClientResponse: Incomplete
    def __init__(self) -> None: ...
    def to_credential(self): ...

class netlmv2:
    username: Incomplete
    domain: Incomplete
    ServerChallenge: Incomplete
    ClientResponse: Incomplete
    ChallengeFromClinet: Incomplete
    def __init__(self) -> None: ...
    def to_credential(self): ...

class netntlm_ess:
    credentials: Incomplete
    ServerChallenge: Incomplete
    LMResponse: Incomplete
    NTResponse: Incomplete
    SessionBaseKey: Incomplete
    def __init__(self) -> None: ...
    def calc_key_exchange_key(self): ...
    @staticmethod
    def construct(server_challenge, client_challenge, credentials): ...
    def to_credential(self): ...
    def calc_session_base_key(self, creds, credtype: str = 'plain'): ...

class netntlm:
    credentials: Incomplete
    ServerChallenge: Incomplete
    LMResponse: Incomplete
    NTResponse: Incomplete
    SessionBaseKey: Incomplete
    def __init__(self) -> None: ...
    def calc_key_exchange_key(self, with_lm: bool = False, non_nt_session_key: bool = False): ...
    @staticmethod
    def construct(server_challenge, credentials): ...
    def to_credential(self): ...
    def calc_session_base_key(self, creds, credtype: str = 'plain'): ...

class netntlmv2:
    credentials: Incomplete
    ServerChallenge: Incomplete
    LMResponse: Incomplete
    NTResponse: Incomplete
    SessionBaseKey: Incomplete
    def __init__(self) -> None: ...
    def calc_key_exchange_key(self): ...
    def calc_key_exhange_key_server(self, credentials): ...
    @staticmethod
    def construct(server_challenge, client_challenge, server_details, credentials, timestamp: Incomplete | None = None): ...
    def to_credential(self): ...

def LMOWFv1(password): ...
def NTOWFv1(password): ...
def LMOWFv2(Passwd, User, UserDom, PasswdHash: Incomplete | None = None): ...
def NTOWFv2(Passwd, User, UserDom, PasswdHash: Incomplete | None = None): ...
def DESL(K, D):
    """
\tIndicates the encryption of an 8-byte data item D with the 16-byte key K
\tusing the Data Encryption Standard Long (DESL) algorithm.
\tThe result is 24 bytes in length.
\t:param K:
\t:param D:
\t:return:
\t"""
