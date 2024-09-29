from octopwn.servers.relay.common.authentication.ntlm.creds_calc import *
from _typeshed import Incomplete
from octopwn.servers.relay.common.authentication.ntlm.common.serverinfo import NTLMServerInfo as NTLMServerInfo
from octopwn.servers.relay.common.authentication.ntlm.messages.authenticate import NTLMAuthenticate as NTLMAuthenticate
from octopwn.servers.relay.common.authentication.ntlm.messages.challenge import NTLMChallenge as NTLMChallenge
from octopwn.servers.relay.common.authentication.ntlm.messages.negotiate import NTLMNegotiate as NTLMNegotiate
from octopwn.servers.relay.common.authentication.ntlm.settings import NTLMClientSettings as NTLMClientSettings
from octopwn.servers.relay.common.authentication.ntlm.structures.avpair import AVPAIRType as AVPAIRType, AVPair as AVPair, MsvAvFlags as MsvAvFlags
from octopwn.servers.relay.common.authentication.ntlm.structures.negotiate_flags import NegotiateFlags as NegotiateFlags
from octopwn.servers.relay.common.authentication.ntlm.structures.ntlmssp_message_signature import NTLMSSP_MESSAGE_SIGNATURE as NTLMSSP_MESSAGE_SIGNATURE
from octopwn.servers.relay.common.authentication.ntlm.structures.ntlmssp_message_signature_noext import NTLMSSP_MESSAGE_SIGNATURE_NOEXT as NTLMSSP_MESSAGE_SIGNATURE_NOEXT
from octopwn.servers.relay.common.authentication.ntlm.structures.version import Version as Version
from octopwn.servers.relay.common.authentication.ntlm.templates.client import NTLMClientTemplates as NTLMClientTemplates
from octopwn.servers.relay.common.authentication.ntlm.templates.server import NTLMServerTemplates as NTLMServerTemplates

class NTLMRelayHandler:
    log_id: Incomplete
    log_q: Incomplete
    client_settings: Incomplete
    force_signdisable: bool
    dropmic: bool
    dropmic2: bool
    modify_negotiate_cb: Incomplete
    modify_challenge_cb: Incomplete
    modify_authenticate_cb: Incomplete
    flags: Incomplete
    challenge: Incomplete
    ntlmNegotiate: Incomplete
    ntlmChallenge: Incomplete
    ntlmAuthenticate: Incomplete
    ntlmNegotiate_raw: Incomplete
    ntlmChallenge_raw: Incomplete
    ntlmAuthenticate_raw: Incomplete
    ntlmNegotiate_server: Incomplete
    ntlmChallenge_server: Incomplete
    ntlmAuthenticate_server: Incomplete
    ntlmNegotiate_server_raw: Incomplete
    ntlmChallenge_server_raw: Incomplete
    ntlmAuthenticate_server_raw: Incomplete
    EncryptedRandomSessionKey: Incomplete
    RandomSessionKey: Incomplete
    SessionBaseKey: Incomplete
    KeyExchangeKey: Incomplete
    SignKey_client: Incomplete
    SealKey_client: Incomplete
    SignKey_server: Incomplete
    SealKey_server: Incomplete
    iteration_cnt: int
    ntlm_credentials: Incomplete
    extra_info: Incomplete
    negotiate_evt: Incomplete
    challenge_evt: Incomplete
    authenticate_evt: Incomplete
    start_client_evt: Incomplete
    def __init__(self, log_q: Incomplete | None = None) -> None: ...
    def setup(self, log_q: Incomplete | None = None) -> None:
        """
\t\tThis must be called before any actual operations.
\t\t"""
    def change_client_settings(self, settings: NTLMClientSettings): ...
    def is_guest(self): ...
    def set_sign(self, tf: bool = True) -> None: ...
    def set_seal(self, tf: bool = True) -> None: ...
    def set_version(self, tf: bool = True) -> None: ...
    def set_kex(self, tf: bool = True) -> None: ...
    def is_extended_security(self): ...
    def signing_needed(self): ...
    def encryption_needed(self): ...
    def get_extra_info(self): ...
    def MAC(self, handle, signingKey, seqNum, message) -> None:
        """
\t\tNot possible to perform this function due to unknown keys during relaying
\t\t"""
    def SEAL(self, signingKey, sealingKey, messageToSign, messageToEncrypt, seqNum, cipher_encrypt) -> None:
        """
\t\tNot possible to perform this function due to unknown keys during relaying
\t\t"""
    def SIGN(self, signingKey, message, seqNum, cipher_encrypt) -> None:
        """
\t\tNot possible to perform this function due to unknown keys during relaying
\t\t"""
    def calc_sealkey(self, mode: str = 'Client') -> None:
        """
\t\tNot possible to perform this function due to unknown keys during relaying
\t\t"""
    def calc_signkey(self, mode: str = 'Client') -> None:
        """
\t\tNot possible to perform this function due to unknown keys during relaying
\t\t"""
    def get_session_key(self): ...
    def get_sealkey(self, mode: str = 'Client'): ...
    def get_signkey(self, mode: str = 'Client'): ...
    async def log_async(self, level, msg) -> None: ...
    def terminate(self) -> None: ...
    async def modify_negotiate(self):
        """
\t\tBy default we don't modify the structures because there can be all kinds of integrity protections.
\t\tHowever, if you find some cool stuff then you can just populate the modify_negotiate_cb in the settings, 
\t\tbut you MUST return both ntlmNegotiate and ntlmNegotiate_raw structures and/or indicate an error 
\t\twhich must be of class Exception!
\t\t"""
    async def modify_challenge(self):
        """
\t\tBy default we don't modify the structures because there can be all kinds of integrity protections.
\t\tHowever, if you find some cool stuff then you can just populate the modify_authenticate_cb in the settings, 
\t\tbut you MUST return both ntlmChallenge_server and ntlmChallenge_server_raw structures and/or indicate an error 
\t\twhich must be of class Exception!
\t\t"""
    async def modify_authenticate(self):
        """
\t\tBy default we don't modify the structures because there can be all kinds of integrity protections.
\t\tHowever, if you find some cool stuff then you can just populate the modify_authenticate_cb in the settings, 
\t\tbut you MUST return both ntlmAuthenticate and ntlmAuthenticate_raw structures and/or indicate an error 
\t\twhich must be of class Exception!
\t\t"""
    async def authenticate_relay_server(self, authdata):
        """
\t\tThis function is to be called by the server side which we obtain the auth material from
\t\t"""
    async def authenticate(self, authData, flags: Incomplete | None = None, seq_number: int = 0, is_rpc: bool = False):
        """
\t\tFRONT TOWARD ENEMY
\t\tThis function is to be called by the client side.
\t\t"""
