from _typeshed import Incomplete
from glob import glob as glob
from octopwn.clients.scannerbase import ScannerConsoleBase as ScannerConsoleBase
from octopwn.common.credential import Credential as Credential
from octopwn.common.utils import convert_bool as convert_bool, create_random_file as create_random_file, hexdump as hexdump, isint as isint

class ROADToolsUtil(ScannerConsoleBase):
    params: Incomplete
    def __init__(self, client_id, connection, cmd_q, msg_queue, prompt, octopwnobj) -> None: ...
    async def store_token(self, username, token, to_print: bool = True) -> None: ...
    async def requestproxy(self, url, method, headers, data: Incomplete | None = None, restype: str = 'json', reqtype: Incomplete | None = None, allow_redirects: bool = True, cookies: Incomplete | None = None, **kwargs): ...
    async def get_auth_obj(self):
        """Get the auth object"""
    async def do_userpass(self, username: str, password: str):
        """Fetches the token for the given username and password"""
    async def do_userpassv2(self, username: str, password: str, scope: str = None):
        """Fetches the token for the given username and password and scope. If scope is not set, it will use the scope parameter or the scope set in the object. If no scope is set, it will fail."""
    async def do_userdiscovery(self, username: str):
        """Discover the user information for the given username"""
    async def do_authrefreshtoken(self, token: str): ...
    async def do_gather(self, token: str, mfa: bool = False, skipfirst: bool = False):
        """ROADrecon - Gather Azure AD information"""
    async def do_xlsexport(self, dbfile: str, outformat: str = 'xlsx', verbose: bool = False):
        """Export data to an Excel file"""
    async def do_policies(self, dbfile: str):
        """Parse Conditional Access policies and export those to a file called caps.html"""
