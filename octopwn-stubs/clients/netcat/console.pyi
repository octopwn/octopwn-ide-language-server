from _typeshed import Incomplete
from aiosmb import logger as logger
from asysocks.common.comms import SocksQueueComms as SocksQueueComms
from octopwn.clients.base import ClientConsoleBase as ClientConsoleBase

class NetCatClient(ClientConsoleBase):
    client: Incomplete
    connection: Incomplete
    target: Incomplete
    encoding: str
    lineterm: str
    binprint: bool
    datareader_task: Incomplete
    def __init__(self, client_id, connection, cmd_q, msg_queue, prompt, octopwnobj) -> None: ...
    async def start(self): ...
    logon_ok: bool
    async def do_disconnect(self) -> None:
        """Disconnects from the target"""
    async def do_connect(self):
        """Connects to the target"""
    async def send(self, data): ...
    async def do_send(self, data: str):
        """Sends a string encoded by 'encoding' to the socket"""
    async def do_sendhex(self, data: str):
        """Sends a hex-encoded binary data to the socket. WARNING! Doesn't add line terminator!"""
    async def do_sendfile(self, filepath: str, blocksize: int = 1024):
        """Reads a file in blocksize and send it to the server"""
    async def do_encoding(self, encoding: str = '') -> None:
        """Sets or gets the text encoding for incoming and outgoing text data"""
    async def do_lineterm(self, lineterm: str = '') -> None:
        """Sets or gets the line terminator for outgoing text data"""
    async def do_binprint(self, binprint: str = '') -> None:
        """Enables binary print. Incoming data will be printed as hexdump
Use '1' to enable
Use '0' to disable
"""
