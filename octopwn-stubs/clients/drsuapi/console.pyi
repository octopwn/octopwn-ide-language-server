from _typeshed import Incomplete
from aiosmb import logger as logger
from octopwn.clients.base import ClientConsoleBase as ClientConsoleBase
from octopwn.common.parsers.ntds import store_ntds_secrets as store_ntds_secrets

class DCEDRSUAPIClient(ClientConsoleBase):
    drsuapi: Incomplete
    connection: Incomplete
    credential: Incomplete
    target: Incomplete
    proxy: Incomplete
    def __init__(self, client_id, connection, cmd_q, msg_queue, prompt, octopwnobj) -> None: ...
    async def start(self): ...
    logon_ok: bool
    async def do_login(self):
        """Connect + login"""
    async def do_logout(self):
        """Logs out from the current session, disconnects from the server"""
    async def do_dcsync(self, username: str, to_print: bool = True, h_token: int = None):
        """Dumps remote secrets using DCSync"""
