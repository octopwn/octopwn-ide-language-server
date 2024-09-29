from _typeshed import Incomplete
from collections.abc import Generator
from jackdaw.dbmodel.edge import Edge as Edge
from jackdaw.dbmodel.netsession import NetSession as NetSession
from jackdaw.nest.graph.construct import GraphConstruct as GraphConstruct
from jackdaw.nest.graph.domaindiff import DomainDiff as DomainDiff
from octopwn.clients.scannerbase import ScannerConsoleBase as ScannerConsoleBase
from octopwn.common.utils import create_random_filepath as create_random_filepath, hexdump as hexdump
from octopwn.remote.protocol.python import jackdaw_pb2 as jackdaw_pb2

def exclude_parse(exclude): ...

class JackdawUtil(ScannerConsoleBase):
    graph_cache_dir: Incomplete
    graphdata_format: str
    db_session: Incomplete
    graph: Incomplete
    graphid: Incomplete
    sqlitefile: Incomplete
    current_adid: Incomplete
    def __init__(self, client_id, connection, cmd_q, msg_queue, prompt, octopwnobj) -> None: ...
    async def do_pathapi(self, msgjson) -> None: ...
    async def do_chgraphdir(self, graph_cache_dir) -> None:
        """Changes graphcache directory"""
    async def do_bhimport(self, bhfile):
        """Import data gathered via BloodHound. Creates a new DB"""
    async def do_dbload(self, sqlitefile, force_load: bool = False):
        """Loads SQLITE database"""
    async def do_graphload(self, graphid, cachefile: Incomplete | None = None):
        """Loads SQLITE database, generates graph cache file"""
    async def pathprint(self, paths) -> None:
        """Takes a list of paths and prints them in a user-friendly command"""
    def curdomains(self) -> Generator[Incomplete, None, None]: ...
    async def do_pathdcsync(self, excludededges: Incomplete | None = None, to_print: bool = True):
        """Nodes with dcsync access"""
    async def do_pathkerberoastda(self, excludededges: Incomplete | None = None, to_print: bool = True):
        """Paths from kerberoastable users to DA"""
    async def do_pathasrepda(self, excludededges: Incomplete | None = None, to_print: bool = True):
        """Path from asreproastable users to DA"""
    async def do_pathhvtda(self, excludededges: Incomplete | None = None, to_print: bool = True):
        """Path to HVT from anywhere"""
    async def do_pathownedda(self, excludededges: Incomplete | None = None, to_print: bool = True):
        """Path from owned users to DA"""
    async def do_pathfromowned(self, excludededges: Incomplete | None = None, to_print: bool = True):
        """Path from owned users to anywhere"""
    async def do_pathgettaggednodes(self, tag: str, to_print: bool = True):
        """Returns a list of tagged nodes"""
    async def do_pathownedhvt(self, excludededges: Incomplete | None = None, to_print: bool = True):
        """Path from owned users to HVT"""
    async def do_pathkerberoastany(self, excludededges: Incomplete | None = None, to_print: bool = True):
        """Path from kerberoastable users to anywhere"""
    def parse_excludededges(self, excludededges): ...
    async def do_pathtoda(self, excludededges: str = None, to_print: bool = True):
        """Calculates shortest path to DA"""
    async def do_path(self, src: str = None, dst: str = None, excludededges: Incomplete | None = None, maxhops: Incomplete | None = None, to_print: bool = True):
        """Calculates shortest path between src and dst SIDs."""
    async def do_oid(self, oid, otype: Incomplete | None = None, to_print: bool = True):
        """Resolves OID (SID) to the actual object"""
    async def do_graphids(self, to_print: bool = True):
        """Lists available Graph IDs"""
    async def do_adids(self, to_print: bool = True):
        """Lists available domain IDs"""
    async def do_currentad(self, to_print: bool = True):
        """Returns the current AD ID"""
    async def do_changead(self, adid, to_print: bool = True):
        """Changes the current AD ID"""
    async def do_trusts(self, to_print: bool = True):
        """Lists AD trusts for current ADID"""
    async def do_kerberoast(self, to_print: bool = True):
        """Lists spn/asreproast tickets"""
    async def do_graphsetowned(self, oid, to_print: bool = True):
        """Sets given OID as owned"""
    async def do_graphclearowned(self, oid, to_print: bool = True):
        """Clears owned status for OID"""
    async def do_grapthsethvt(self, oid, to_print: bool = True):
        """Sets HVT status for OID"""
    async def do_graphclearhvt(self, oid, to_print: bool = True):
        """Clears HVT status for OID"""
    async def do_shares(self, to_print: bool = True):
        """Lists non-default shares"""
    async def do_dns(self, ip_or_hostname: str, to_print: bool = True):
        """Looks up IP or hostname"""
    async def do_dcsyncaiosmb(self, dumpfile, to_print: bool = True):
        """Uploads a dcsync file to the DB (aiosmb format) """
    async def do_dcsyncimpacket(self, dumpfile, to_print: bool = True):
        """Uploads a dcsync file to the DB (impacket format) """
    async def do_potfile(self, potfile, to_print: bool = True):
        """Uploads hashcat potfile to the DB"""
    async def do_pwuncracked(self, hashtype: str = 'nt', to_print: bool = False):
        """Uploads hashcat potfile to the DB"""
    async def do_pwcracked(self, to_print: bool = False):
        """Lists all cracked user (with extra info)"""
    async def do_pwsharing(self, to_print: bool = True):
        """Lists all users having the same password"""
    async def do_pwstats(self, to_print: bool = True):
        """Generates all pw stats"""
    async def do_pwreport(self, to_print: bool = True): ...
    async def do_search(self, text, h_clientid: Incomplete | None = None, h_token: Incomplete | None = None): ...
