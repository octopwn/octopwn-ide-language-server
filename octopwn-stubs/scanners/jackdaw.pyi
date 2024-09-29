from _typeshed import Incomplete
from octopwn.clients.scannerbase import ScannerConsoleBase as ScannerConsoleBase

class JackdawScanner(ScannerConsoleBase):
    params: Incomplete
    ext_result_q: Incomplete
    graph_id: Incomplete
    enumerator_task: Incomplete
    monitor_task: Incomplete
    db_session: Incomplete
    db_dumped: bool
    progress_types: Incomplete
    def __init__(self, client_id, connection, cmd_q, msg_queue, prompt, octopwnobj) -> None: ...
    async def dumpdb(self) -> None: ...
    async def stop(self): ...
    enumerator: Incomplete
    async def scan(self, h_token: Incomplete | None = None, h_clientid: Incomplete | None = None):
        """Start enumeration"""
