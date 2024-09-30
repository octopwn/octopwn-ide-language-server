import datetime
from _typeshed import Incomplete
from octopwn.clients.base import ClientConsoleBase as ClientConsoleBase
from octopwn.common.clientconfig import ScannerConfig as ScannerConfig
from octopwn.common.paramsutil import serializeParamsDict as serializeParamsDict
from octopwn.common.target import Target as Target
from octopwn.common.utils import create_table as create_table, isint as isint
from octopwn.remote.protocol.python import messages_pb2 as messages_pb2

class ProgressChanged:
    current: Incomplete
    total: Incomplete
    label: Incomplete
    last_update: Incomplete
    percentage: int
    speed_str: str
    def __init__(self, current, total, label, last_update: Incomplete | None = None, last_update_cnt: Incomplete | None = None) -> None: ...
    def to_dict(self): ...
    def to_json(self): ...

class ScannerConsoleBase(ClientConsoleBase):
    doc_header: str
    params: Incomplete
    scan_running_evt: Incomplete
    def __init__(self, client_id, connection, cmd_q, msg_queue, prompt, octopwnobj, command_modifier: Incomplete | None = None) -> None: ...
    def load_config(self, scannerconfig: ScannerConfig): ...
    def deserialize_params(self, sparams): ...
    def deserialize_history(self, history): ...
    def save_config(self, scannerconfig: ScannerConfig): ...
    def serialize_history(self, history): ...
    def save_params(self, params: Incomplete | None = None): ...
    def get_options_json(self): ...
    async def do_options(self):
        """Lists editable parameters"""
    async def do_clearparam(self, parameter):
        """Resets parameters to original state. Only list currently!"""
    async def do_showparam(self, parameter, to_print: bool = True): ...
    async def setparam_targets(self, targetid: str): ...
    async def do_setparam(self, parameter: str, value: str, to_print: bool = True):
        """Updates an editable parameter"""
    async def remoteres(self, tid, msg, remote_clientid: Incomplete | None = None): ...
    async def add_target(self, val, source: str = 'SCANNER'): ...
    def copyparams(self):
        """Return a copy of the params dict without the internal params"""
    async def do_scan(self, h_token: Incomplete | None = None, h_clientid: Incomplete | None = None):
        """Start enumeration"""
    async def do_stop(self, finished: bool = False, h_token: Incomplete | None = None, h_clientid: Incomplete | None = None):
        """Stops the scan"""
    def is_running(self):
        """Returns True if the scan is running"""
    async def start(self):
        """Overriding start by default, so this will get invoked from ClientBase"""
    async def progresschanged(self, current: int, total: int, label: str, last_update: datetime.datetime = None, last_update_cnt: int = None, h_token: int = None):
        """Call this to indicate progress"""
    async def scannerresult(self, restype, result, resline, host, tid, h_token: int = None, h_clientid: int = None):
        """Call this to send a result"""
    async def scannerstarted(self, h_token: Incomplete | None = None, h_clientid: Incomplete | None = None) -> None: ...
    async def scannerfinished(self, finished, h_token: Incomplete | None = None, h_clientid: Incomplete | None = None) -> None: ...
