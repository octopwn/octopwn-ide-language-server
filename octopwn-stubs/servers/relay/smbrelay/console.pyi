from _typeshed import Incomplete
from aiosmb.relay.serverconnection import SMBRelayServerConnection as SMBRelayServerConnection
from asyauth.protocols.ntlm.relay.native import NTLMRelaySettings as NTLMRelaySettings
from asysocks.unicomm.common.proxy import UniProxyTarget as UniProxyTarget
from octopwn.clients.scannerbase import ScannerConsoleBase as ScannerConsoleBase

class SMBRelayServer(ScannerConsoleBase):
    params: Incomplete
    serverproto: Incomplete
    servertransport: Incomplete
    auth_relay_queue: Incomplete
    server_task: Incomplete
    def __init__(self, client_id, connection, cmd_q, msg_queue, prompt, octopwnobj) -> None: ...
    async def start(self): ...
    async def handle_relay(self) -> None: ...
    async def do_serve(self): ...
    async def stop(self): ...
