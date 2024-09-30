from _typeshed import Incomplete
from octopwn.clients.scannerbase import ScannerConsoleBase as ScannerConsoleBase
from octopwn.common.credential import Credential as Credential
from octopwn.common.parsers.lsass import store_lsass_creds as store_lsass_creds
from octopwn.common.parsers.ntds import store_ntds_secrets as store_ntds_secrets
from octopwn.common.parsers.registry import store_registry_creds as store_registry_creds
from octopwn.common.utils import isint as isint
from pypykatz.commons.common import UniversalEncoder as UniversalEncoder

class AsyncFile:
    filename: Incomplete
    fhandle: Incomplete
    def __init__(self, filename) -> None: ...
    async def read(self, n: int = -1): ...
    async def seek(self, n, beg: int = 0): ...
    def tell(self): ...

class PypykatzUtil(ScannerConsoleBase):
    doc_header: str
    ntds_process_task: Incomplete
    ntds_parser_task: Incomplete
    def __init__(self, client_id, connection, cmd_q, msg_queue, prompt, octopwnobj) -> None: ...
    async def do_locallsass(self):
        """Not yet implemented!"""
    async def process_kerberos_session(self, ksessions) -> None: ...
    async def lsass_print(self, results): ...
    async def do_lsass(self, minidumpfile):
        """Parses an LSASS dump file"""
    async def do_registry(self, system, sam: Incomplete | None = None, security: Incomplete | None = None, software: Incomplete | None = None):
        """Parses the resitry hive files, print secrets"""
    async def do_ntds(self, systemhive, ntdsfile, outfile=..., progress_cb: Incomplete | None = None):
        """Parses NTDS.DIT file"""
    async def do_gppassword(self, pw_enc_b64):
        """Decrypts GPPassword"""
    async def do_nt(self, password, to_print: bool = True):
        """Calculates NT hash of password"""
    async def do_lm(self, password, to_print: bool = True):
        """Calculates LM hash of password"""
    async def do_msdcc(self, username, password, to_print: bool = True):
        """Calculates version 1 of MS Domain Cached Credentials hash from username and password"""
    async def do_msdcc2(self, username, password, iteration: int = 10240, to_print: bool = True):
        """Calculates version 2 of MS Domain Cached Credentials hash from username and password"""
    async def do_kerberos(self, username, password, domain: Incomplete | None = None, to_print: bool = True):
        """Calculates kerberos keys from username and password and domain"""
    async def do_hashes(self, username, password, domain: Incomplete | None = None):
        """Calculates common hashes from username,password and optionally domain"""
    async def do_ofscan(self, encdata_or_file) -> None:
        """Decrypts data from Trendmicro ofscan.ini file"""
