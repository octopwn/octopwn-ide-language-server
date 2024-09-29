from _typeshed import Incomplete
from octopwn import logger as logger
from octopwn.clients.base import ClientConsoleBase as ClientConsoleBase

class DNSClient(ClientConsoleBase):
    connection: Incomplete
    target: Incomplete
    dnsclient: Incomplete
    def __init__(self, client_id, connection, cmd_q, msg_queue, prompt, octopwnobj) -> None: ...
    async def start(self): ...
    async def do_query(self, name: str, qtype: str = None, to_print: bool = True, h_token: int = None):
        """Perform a DNS query"""
