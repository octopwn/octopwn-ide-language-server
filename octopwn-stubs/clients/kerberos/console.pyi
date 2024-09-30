from _typeshed import Incomplete
from octopwn import logger as logger
from octopwn.clients.base import ClientConsoleBase as ClientConsoleBase
from octopwn.common.credential import Credential as Credential
from octopwn.common.kerbutils import format_kirbi as format_kirbi
from octopwn.remote.protocol.python import kerberos_pb2 as kerberos_pb2

class KerberosClient(ClientConsoleBase):
    connection: Incomplete
    target: Incomplete
    credential_base: Incomplete
    credential: Incomplete
    def __init__(self, client_id, connection, cmd_q, msg_queue, prompt, octopwnobj) -> None: ...
    async def start(self): ...
    def isint(self, x): ...
    async def do_kerberoast(self, spn: str, crossdomain: bool = False, etype_tgt: int = None, etype_tgs: int = 23, to_print: bool = True, h_token: int = None):
        """Kerberoast user"""
    async def do_asreproast(self, user: str, to_print: bool = True, h_token: int = None):
        """ASREPRoast user. Target is expected in user@FQDN format !OR! Integer denoting an active LDAP client for automatic kerberoast."""
    async def do_tgt(self, etype: Incomplete | None = None, to_print: bool = True, h_token: int = None):
        """Obtains TGT for current user"""
    async def do_tgs(self, spn: str, to_print: bool = True, h_token: int = None):
        """Gets TGS for SPN"""
    async def do_s4uproxy(self, spn, targetuser, to_print: bool = True):
        """S4U proxy. SPN: spn format. targetuser: user@FQDN format"""
    async def do_s4uself(self, targetuser: str, to_print: bool = True):
        """S4U Self. targetuser: user@FQDN format"""
    async def do_nt(self):
        """Gets NT hash from a PKINIT (cert) auth"""
    async def kerberoast_windows(self, targets: str): ...
    async def kerberoast_wsnet(self, targets): ...
    async def do_cve202233679(self, to_print: bool = True, h_token: int = None):
        """Performs the CVE-2020-13379 attack. This attack will return a valid TGT for the current ASREProastable user if the domain is vulnerable."""
