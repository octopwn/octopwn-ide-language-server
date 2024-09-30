from wsnet.protocol import *
from _typeshed import Incomplete
from asyauth.common.constants import asyauthSecret as asyauthSecret
from asyauth.common.credentials import UniCredential as UniCredential
from octopwn.clients.scannerbase import ScannerConsoleBase as ScannerConsoleBase
from octopwn.common.credential import Credential as Credential
from octopwn.common.proxy import Proxy as Proxy
from octopwn.remote.protocol.python import kerberos_pb2 as kerberos_pb2
from octopwn.servers.wsnetws.authproxy import AuthProxy as AuthProxy, AuthProxyKerberosClient as AuthProxyKerberosClient, AuthProxyNTLMClient as AuthProxyNTLMClient
from octopwn.servers.wsnetws.socksproxy import WSNETSocksProxy as WSNETSocksProxy

class WSNETWSAgent(ScannerConsoleBase):
    params: Incomplete
    from_reload: Incomplete
    agentid: str
    ws: Incomplete
    agentinfo: Incomplete
    agentname: str
    credid: Incomplete
    proxyid: Incomplete
    dctargetid: Incomplete
    realm: Incomplete
    dchostname: Incomplete
    closed_evt: Incomplete
    token_table: Incomplete
    def __init__(self, client_id, connection, cmd_q, msg_queue, prompt, octopwnobj, from_reload: bool = False) -> None: ...
    def get_token(self): ...
    async def start(self): ...
    def isint(self, x): ...
    async def do_info(self) -> None: ...
    async def do_applyinfo(self) -> None:
        """Applies default realm and DC ip settings from agent"""
    async def setupproxies(self): ...
    async def do_kerberoast(self, spn: str, to_print: bool = True, h_token: int = None):
        """Kerberoast user"""
    async def do_jackdaw(self, dctarget: Incomplete | None = None, h_token: int = None, h_clientid: int = None): ...
    def create_authproxy(self): ...
    def create_proxy(self): ...
    def build_context(self, credential: UniCredential): ...
