from _typeshed import Incomplete
from octopwn.clients.scannerbase import ScannerConsoleBase as ScannerConsoleBase
from octopwn.common.target import Target as Target
from octopwn.common.utils import don as don

class NmapUtil(ScannerConsoleBase):
    xmlfile: Incomplete
    scan: Incomplete
    def __init__(self, client_id, connection, cmd_q, msg_queue, prompt, octopwnobj) -> None: ...
    async def do_load(self, filepath):
        """Loads a nmap xml file"""
    def get_host_addr(self, host, addrtype: str = 'any'):
        """returns the first address for the given host of given addresstype"""
    def ports_per_host(self, host): ...
    async def do_hosts(self, to_print: bool = True):
        """Lists all hostnames from scanfile"""
    async def do_ips(self, to_print: bool = True):
        """Lists all hostnames from scanfile"""
    async def do_ports(self, to_print: bool = True):
        """Lists all IP:PORT entries found by NMAP"""
    async def do_services(self, to_print: bool = True):
        """Generates a table with all services found by NMAP"""
    async def do_addtargets(self):
        """Populates the target list in octopwn with the IP addresses found in this scan file"""
