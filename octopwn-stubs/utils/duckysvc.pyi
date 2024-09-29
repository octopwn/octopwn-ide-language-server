from _typeshed import Incomplete
from octopwn.clients.scannerbase import ScannerConsoleBase as ScannerConsoleBase

class DuckySvcUtil(ScannerConsoleBase):
    params: Incomplete
    def __init__(self, client_id, connection, cmd_q, msg_queue, prompt, octopwnobj) -> None: ...
    async def do_type(self, string, to_print: bool = True):
        """Sends a ducky script command to the DuckySvc server"""
    async def do_typefile(self, filepath, to_print: bool = True):
        """Sends a duckyscript file (line-by-line) to the DuckySvc server"""
