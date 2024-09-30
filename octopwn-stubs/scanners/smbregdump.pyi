from _typeshed import Incomplete
from aiosmb.commons.connection.factory import SMBConnectionFactory as SMBConnectionFactory
from octopwn.clients.scannerbase import ScannerConsoleBase as ScannerConsoleBase
from octopwn.common.parsers.registry import store_registry_creds as store_registry_creds
from octopwn.remote.protocol.python import messages_pb2 as messages_pb2, smb_pb2 as smb_pb2

class SMBRegdumpResult:
    regsecrets: Incomplete
    def __init__(self, regsecrets) -> None: ...
    def to_line(self, separator: str = '\t'): ...

class SMBRegdumpExecutor:
    factory: Incomplete
    srvwaittime: Incomplete
    def __init__(self, factory: SMBConnectionFactory, srvwaittime: int = 4) -> None: ...
    async def run(self, targetid, target, out_queue): ...

class SMBRegdumpScanner(ScannerConsoleBase):
    params: Incomplete
    enumerator_task: Incomplete
    monitor_task: Incomplete
    results_ctr: int
    total_ctr: int
    def __init__(self, client_id, connection, cmd_q, msg_queue, prompt, octopwnobj) -> None: ...
    async def stop(self): ...
    enumerator: Incomplete
    async def scan(self, h_token: Incomplete | None = None, h_clientid: Incomplete | None = None):
        """Start enumeration"""
