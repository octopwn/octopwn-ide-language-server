from _typeshed import Incomplete
from octopwn.clients.scannerbase import ScannerConsoleBase as ScannerConsoleBase
from octopwn.common.utils import UniversalEncoder as UniversalEncoder

class SQLITEUtil(ScannerConsoleBase):
    dbconn: Incomplete
    def __init__(self, client_id, connection, cmd_q, msg_queue, prompt, octopwnobj) -> None: ...
    def strtrim(self, x, maxlen: Incomplete | None = None): ...
    async def do_load(self, filename):
        """Loads a sqlite database file"""
    async def do_tables(self, to_print: bool = True):
        """Lists all tables in the database"""
    async def do_columns(self, tablename, to_print: bool = True):
        """Lists all columns of a table"""
    async def do_readtable(self, tablename, numrec: int = 1000, offset: int = 0, to_trim: Incomplete | None = None, to_print: bool = True, to_send: bool = True):
        """Reads a table from the database"""
    async def do_query(self, query, to_trim: Incomplete | None = None, to_print: bool = True):
        """Executes a SQL query"""
