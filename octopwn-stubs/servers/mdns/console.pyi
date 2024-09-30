from _typeshed import Incomplete
from octopwn.clients.scannerbase import ScannerConsoleBase as ScannerConsoleBase
from octopwn.servers.protocols.DNS import DNSAAAAResource as DNSAAAAResource, DNSAResource as DNSAResource, DNSPacket as DNSPacket, DNSResponse as DNSResponse, DNSType as DNSType

class MDNSServer(ScannerConsoleBase):
    params: Incomplete
    server_task: Incomplete
    def __init__(self, client_id, connection, cmd_q, msg_queue, prompt, octopwnobj) -> None: ...
    async def start(self): ...
    async def do_serve(self): ...
    async def do_spoof(self) -> None: ...
    async def do_spooftarget(self, target, ip: str = 'SELF') -> None: ...
    async def stop(self): ...
