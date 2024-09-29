from _typeshed import Incomplete
from octopwn.clients.scannerbase import ScannerConsoleBase as ScannerConsoleBase
from octopwn.remote.protocol.python import messages_pb2 as messages_pb2, rdp_pb2 as rdp_pb2

class RDPLoginScanner(ScannerConsoleBase):
    params: Incomplete
    ext_result_q: Incomplete
    enumerator_task: Incomplete
    monitor_task: Incomplete
    def __init__(self, client_id, connection, cmd_q, msg_queue, prompt, octopwnobj) -> None: ...
    async def stop(self): ...
    enumerator: Incomplete
    async def scan(self, h_token: Incomplete | None = None, h_clientid: Incomplete | None = None):
        """Start enumeration"""
