import ssl
import websockets
from _typeshed import Incomplete
from octopwn.core import OctoPwn as OctoPwn
from octopwn.remote.protocol.python import messages_pb2 as messages_pb2
from octopwn.remote.server import logger as logger
from octopwn.remote.server.authentication import AuthHandler as AuthHandler, UserAuthError as UserAuthError
from octopwn.remote.server.screenhandler import RemoteScreenHandler as RemoteScreenHandler

class RemoteClientHandler:
    client_id: Incomplete
    ws: Incomplete
    octopwn: Incomplete
    def __init__(self, client_id: int, ws: websockets, octopwn) -> None: ...
    async def cleanup(self) -> None: ...

class RemoteServer:
    listen_ip: Incomplete
    listen_port: Incomplete
    listen_sslctx: Incomplete
    is_shared: Incomplete
    workdir: Incomplete
    clients: Incomplete
    history_save_time: int
    history_save_location: Incomplete
    plugins: Incomplete
    mtod: Incomplete
    license_file: Incomplete
    license_plugins: Incomplete
    authentication_handler: Incomplete
    def __init__(self, listen_ip: str = '127.0.0.1', listen_port: int = 8181, listen_sslctx: ssl.SSLContext = None, is_shared: bool = True, workdir: str = './', authhandler: AuthHandler = None, plugins: list[str] = None, motd: str = None, license_file: str = None, license_plugins: str = None) -> None: ...
    def get_clientid(self): ...
    async def load_previous_state(self): ...
    async def run(self) -> None: ...
