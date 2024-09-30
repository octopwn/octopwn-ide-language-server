from _typeshed import Incomplete
from octopwn.clients.scannerbase import ScannerConsoleBase as ScannerConsoleBase
from octopwn.common.target import Target as Target
from octopwn.common.utils import don as don

class MasscanUtil(ScannerConsoleBase):
    xmlfile: Incomplete
    tree: Incomplete
    root: Incomplete
    hosts: Incomplete
    def __init__(self, client_id, connection, cmd_q, msg_queue, prompt, octopwnobj) -> None: ...
    async def do_load(self, filepath):
        """Loads a masscan xml file"""
    async def do_addtargets(self):
        """Populates the target list in octopwn with the IP addresses found in this scan file"""
