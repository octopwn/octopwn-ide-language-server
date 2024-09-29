from _typeshed import Incomplete
from asysocks.unicomm.protocol.client.http.commons.target import HTTPTarget as HTTPTarget
from awinrm import logger as logger
from octopwn.clients.base import ClientConsoleBase as ClientConsoleBase

class WinRMClient(ClientConsoleBase):
    connection: Incomplete
    target: Incomplete
    credential: Incomplete
    authproto: Incomplete
    client: Incomplete
    def __init__(self, client_id, connection, cmd_q, msg_queue, prompt, octopwnobj) -> None: ...
    async def start(self): ...
    logon_ok: bool
    async def do_logout(self):
        """Logout"""
    async def do_cmdexec(self, command: str):
        """Execute a command"""
