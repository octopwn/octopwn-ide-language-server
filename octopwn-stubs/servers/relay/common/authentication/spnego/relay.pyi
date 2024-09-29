from octopwn.servers.relay.common.authentication.spnego.asn1_structs import *
from _typeshed import Incomplete

class SPNEGORelay:
    authentication_contexts: Incomplete
    selected_authentication_context: Incomplete
    selected_authentication_context_server: Incomplete
    selected_mechtype: Incomplete
    selected_mechtype_server: Incomplete
    iteration_ctr: int
    start_client_evt: Incomplete
    iteration_ctr_server: int
    mic_data: Incomplete
    def __init__(self) -> None: ...
    def setup(self, log_q: Incomplete | None = None) -> None: ...
    def is_guest(self): ...
    async def sign(self, data, message_no, direction: str = 'init'): ...
    async def encrypt(self, data, message_no): ...
    async def decrypt(self, data, message_no, direction: str = 'init', auth_data: Incomplete | None = None): ...
    def get_ntlm(self): ...
    def add_auth_context(self, name, ctx) -> None:
        """
\t\tAdd an authentication context to the given authentication context name.
\t\tValid names are:
\t\t\t'NTLMSSP - Microsoft NTLM Security Support Provider'
\t\t\t'MS KRB5 - Microsoft Kerberos 5'
\t\t\t'KRB5 - Kerberos 5'
\t\t\t'KRB5 - Kerberos 5 - User to User'
\t\t\t'NEGOEX - SPNEGO Extended Negotiation Security Mechanism'
\t\t\t
\t\tContext MUST be already set up!
\t\t"""
    def select_common_athentication_type(self, mech_types): ...
    async def process_ctx_authenticate_server(self, token_data, include_negstate: bool = False, flags: Incomplete | None = None, seq_number: int = 0, is_rpc: bool = False): ...
    async def process_ctx_authenticate(self, token_data, include_negstate: bool = False, flags: Incomplete | None = None, seq_number: int = 0, is_rpc: bool = False): ...
    def get_copy(self): ...
    def list_original_conexts(self):
        """
\t\tReturns a list of authentication context names available to the SPNEGO authentication.
\t\t"""
    def get_original_context(self, ctx_name):
        """
\t\tReturns a copy of the original (not used) authentication context sp[ecified by name.
\t\tYou may use this ctx to perform future authentication, as it has the user credentials
\t\t"""
    def get_extra_info(self): ...
    def get_session_key(self): ...
    def get_mechtypes_list(self): ...
    async def authenticate_relay_server(self, token, flags: Incomplete | None = None, seq_number: int = 0, is_rpc: bool = False): ...
    async def authenticate(self, token, flags: Incomplete | None = None, seq_number: int = 0, is_rpc: bool = False):
        """
\t\tThis function is called (multiple times) during negotiation phase of a protocol to determine hich auth mechanism to be used
\t\tToken is a byte array that is an ASN1 NegotiationToken structure.
\t\t"""
