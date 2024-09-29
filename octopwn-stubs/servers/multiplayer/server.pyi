import ssl
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
    def __init__(self, client_id: int, ws, octopwn) -> None: ...
    async def cleanup(self) -> None: ...

class MultiplayerServer:
    print: Incomplete
    listen_ip: Incomplete
    listen_port: Incomplete
    listen_sslctx: Incomplete
    clients: Incomplete
    history_save_time: int
    history_save_location: Incomplete
    motd: Incomplete
    authentication_handler: Incomplete
    def __init__(self, octopwnobj, print_cb, listen_ip: str = '127.0.0.1', listen_port: int = 8181, listen_sslctx: ssl.SSLContext = None, authhandler: AuthHandler = None, motd: str = None) -> None: ...
    def get_clientid(self): ...
    async def run(self) -> None: ...
