from _typeshed import Incomplete
from octopwn.clients.scannerbase import ScannerConsoleBase as ScannerConsoleBase

class NotesUtil(ScannerConsoleBase):
    params: Incomplete
    def __init__(self, client_id, connection, cmd_q, msg_queue, prompt, octopwnobj) -> None: ...
    async def do_updatetext(self, data: str, to_print: bool = True):
        """Saves text in the persistent store"""
    async def do_getcontent(self, to_print: bool = True):
        """Returns the content"""
    async def do_load(self, fname: str):
        """Loads Markdown formatted text from a file"""
