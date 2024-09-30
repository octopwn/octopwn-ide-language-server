from _typeshed import Incomplete
from asysocks.unicomm.common.scanner.common import ScannerInfo as ScannerInfo
from octopwn.clients.scannerbase import ScannerConsoleBase as ScannerConsoleBase
from octopwn.remote.protocol.python import messages_pb2 as messages_pb2, scanner_pb2 as scanner_pb2

class PortscanResult:
    target: Incomplete
    port: Incomplete
    protocol: Incomplete
    def __init__(self, target, port, protocol: str = 'TCP') -> None: ...
    def to_line(self, separator: str = '\t'): ...

class TCPScannerExecutor:
    proxies: Incomplete
    def __init__(self, proxies) -> None: ...
    async def run(self, targetid, target, out_queue) -> None: ...

class TCPPortScanner(ScannerConsoleBase):
    params: Incomplete
    enumerator_task: Incomplete
    def __init__(self, client_id, connection, cmd_q, msg_queue, prompt, octopwnobj) -> None: ...
    async def stop(self): ...
    enumerator: Incomplete
    async def scan(self, h_token: Incomplete | None = None, h_clientid: Incomplete | None = None):
        """Start enumeration"""
