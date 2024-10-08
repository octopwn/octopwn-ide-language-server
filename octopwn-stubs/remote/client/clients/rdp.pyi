from aardwolf.commons.queuedata import *
from aardwolf.commons.queuedata.constants import MOUSEBUTTON as MOUSEBUTTON, VIDEO_FORMAT as VIDEO_FORMAT
from aardwolf.extensions.RDPECLIP.protocol.formatlist import CLIPBRD_FORMAT as CLIPBRD_FORMAT
from octopwn.remote.client.clients.base import ClientConsoleBaseRemote as ClientConsoleBaseRemote
from octopwn.remote.protocol.python import messages_pb2 as messages_pb2, rdp_pb2 as rdp_pb2

class RDPClientConsoleRemote(ClientConsoleBaseRemote):
    logon_ok: bool
    def __init__(self, octopwnobj, clientid, commands=[]) -> None: ...
    async def mouse_evt(self, x: int, y: int, button: int, press: bool, release: bool): ...
    async def keyboard_evt(self, keychar: str, press: bool, is_scancode: bool = False): ...
    def paste_evt(self, *args) -> None: ...
    async def do_logout(self): ...
    async def do_login(self, resolution: str = '1024x768'): ...
