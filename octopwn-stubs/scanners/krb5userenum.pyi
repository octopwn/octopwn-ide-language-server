from _typeshed import Incomplete
from asysocks.unicomm.client import UniClient as UniClient
from asysocks.unicomm.common.scanner.common import ScannerError as ScannerError, ScannerInfo as ScannerInfo
from asysocks.unicomm.common.target import UniProto as UniProto, UniTarget as UniTarget
from minikerberos.common.spn import KerberosSPN as KerberosSPN
from octopwn.clients.scannerbase import ScannerConsoleBase as ScannerConsoleBase
from octopwn.remote.protocol.python import messages_pb2 as messages_pb2, scanner_pb2 as scanner_pb2

class KRB5UserResult:
    username: Incomplete
    def __init__(self, username) -> None: ...
    def to_line(self, separator: str = '\t'): ...

class KRB5UserEnumExecutor:
    ktarget: Incomplete
    realm: Incomplete
    def __init__(self, ktarget, realm) -> None: ...
    async def run(self, targetid, target, out_queue) -> None: ...

class KRB5UserEnum(ScannerConsoleBase):
    params: Incomplete
    enumerator_task: Incomplete
    def __init__(self, client_id, connection, cmd_q, msg_queue, prompt, octopwnobj) -> None: ...
    async def stop(self): ...
    enumerator: Incomplete
    async def scan(self, h_token: Incomplete | None = None, h_clientid: Incomplete | None = None):
        """Start enumeration"""
