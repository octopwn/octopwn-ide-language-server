from _typeshed import Incomplete
from octopwn.clients.scannerbase import ScannerConsoleBase as ScannerConsoleBase
from octopwn.common.credential import Credential as Credential
from octopwn.common.utils import create_random_file as create_random_file, hexdump as hexdump, isint as isint
from pypykatz import logger as logger
from pypykatz.dpapi.dpapi import DPAPI

class DPAPIUtil(ScannerConsoleBase):
    params: Incomplete
    def __init__(self, client_id, connection, cmd_q, msg_queue, prompt, octopwnobj) -> None: ...
    def create_dpapi_masterkeys(self) -> DPAPI: ...
    async def do_loadcreds(self) -> None:
        """Loads all DPAPI credentials from the Credentials tab"""
    async def do_clearprekeys(self):
        """Clears the prekey cache"""
    async def do_clearmasterkeys(self):
        """Clears the masterkey cache"""
    async def do_prekey_registry(self, systemhive, securityhive, samhive):
        """Extraces prekeys from registry hives"""
    async def do_prekey_password(self, password, usersid):
        """Generates prekeys from users password and SID"""
    async def do_prekey_nt(self, nthash, usersid):
        """Generates prekeys from users NT hash and SID"""
    async def do_minidump(self, minidumpfile, outfile):
        """Extracts all prekeys and masterkeys from LSASS minidump"""
    async def do_masterkeys(self, path: str = '*'):
        """Loads all masterkey files in a directory and automatically decryptes them. Ignores fail"""
    async def do_masterkey(self, masterkeyfile, to_print: bool = True):
        """Decrypts masterkey file using the prekey cache"""
    async def do_credential(self, credfile):
        """Decrypts a credential file (.cred) using cached masterkeys"""
    async def do_vpol(self, vpol):
        """Decrypts a vpol file (.vpol) using cached masterkeys"""
    async def do_vcred(self, vcredfile, vpolkey):
        """Decrypts a vcred file (.vcred) using a corresponding VPOL key (in hex)"""
    async def do_securestring(self, securestring):
        """Decrypts a securestring (in hex format or file path) using cached masterkeys"""
    async def do_blob(self, blob):
        """Decrypts a DPAPI BLOB (in hex format or file path) using cached masterkeys"""
    async def do_wifi(self, wificonfig):
        """Decrypts a wifi config file (.xml) using a previously decrypted masterkey file"""
    async def do_chrome(self, localstate, cookies: Incomplete | None = None, logindata: Incomplete | None = None):
        """Decrypts chrome secrets using the localstate/cookies/logindata files and a previously decrypted masterkey file"""
    async def do_cloudapkd(self, prt_full: None = None):
        """Decrypts a cloudapkd data using a previously decrypted masterkey file. If invoked without arguments, it will decrypt all cloudapkd data. If invoked with an integer, it will decrypt the corresponding credential. If invoked with a string, it will decrypt the PRT directly"""
    async def do_describe(self, datatype, data):
        """Describes (parses) a DPAPI BLOB, Masterkey, VPOL or PVK file"""
