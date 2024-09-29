from _typeshed import Incomplete
from octopwn.clients.scannerbase import ScannerConsoleBase as ScannerConsoleBase
from octopwn.common.clientconfig import UtilsConfig as UtilsConfig
from octopwn.common.utils import create_server_ssl_context as create_server_ssl_context
from octopwn.servers.wsnetws.agent import WSNETWSAgent as WSNETWSAgent

class WSNETServer(ScannerConsoleBase):
    params: Incomplete
    wsserver: Incomplete
    agents: Incomplete
    registered_agents_ctr: int
    agent_dispatch_queue: Incomplete
    def __init__(self, client_id, connection, cmd_q, msg_queue, prompt, octopwnobj) -> None: ...
    async def handle_client(self, ws, path) -> None: ...
    async def stop(self) -> None: ...
    async def do_serve(self) -> None: ...
