from aardwolf.commons.queuedata import *
from _typeshed import Incomplete
from aardwolf import logger as logger
from aardwolf.protocol.x224.constants import SUPP_PROTOCOLS as SUPP_PROTOCOLS
from octopwn.clients.base import ClientConsoleBase as ClientConsoleBase
from octopwn.common.utils import create_random_file as create_random_file
from octopwn.remote.protocol.python import messages_pb2 as messages_pb2, rdp_pb2 as rdp_pb2, smb_pb2 as smb_pb2
from pyodide.ffi import create_proxy as create_proxy

class RDPClient(ClientConsoleBase):
    connection: Incomplete
    target: Incomplete
    credential: Incomplete
    record_fps: int
    record_codec: str
    mouse_cb_proxy: Incomplete
    keyboard_cb_proxy: Incomplete
    paste_cb_proxy: Incomplete
    duckyscriptpath: Incomplete
    remote_clientids: Incomplete
    height: Incomplete
    width: Incomplete
    bpp: Incomplete
    def __init__(self, client_id, connection, cmd_q, msg_queue, prompt, octopwnobj) -> None: ...
    async def start(self): ...
    async def remote_in(self, remote_clientid: int, msg: messages_pb2.OctoClientMessage, username: str = 'default'): ...
    async def mouse_evt(self, x: int, y: int, button: int, press: bool, release: bool): ...
    async def keyboard_evt(self, keychar: str, press: bool, is_scancode: bool = False): ...
    async def ducky_keyboard_sender(self, scancode, is_pressed, as_char: bool = False) -> None: ...
    def paste_evt(self, *args) -> None: ...
    logon_ok: bool
    async def do_login(self, size: str = '1024x768', record: bool = False, h_token: Incomplete | None = None, h_clientid: Incomplete | None = None):
        """Connect + login"""
    async def do_logout(self):
        """Disconnect + logout"""
    async def do_paste(self, text):
        """Set remote clipboard text (PASTE)"""
    async def do_duckyexec(self):
        """Starts ducky script. You'll need to login first!"""
    async def do_screenshot(self):
        """Take screenshot of remote desktop. You'll need to login first!"""
    async def do_duckyfile(self, duckyscriptpath):
        """Sets duckyscript file to use with duckyexec"""
    async def do_pastefile(self, filepath):
        """Pushes text file content to remote clipboard"""
