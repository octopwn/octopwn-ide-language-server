import asyncio
from _typeshed import Incomplete
from octopwn.remote.protocol.python import messages_pb2 as messages_pb2
from octopwn.remote.server import logger as logger
from octopwn.remote.server.authentication import AuthHandler as AuthHandler, UserAuthError as UserAuthError

class AuthHandlerFile(AuthHandler):
    credfile: Incomplete
    credentials: Incomplete
    def __init__(self, credfile, authmethods=['PLAIN', 'CERT']) -> None: ...
    def authenticate(self, msg: messages_pb2.RegisterClient, connection: asyncio.StreamWriter) -> tuple[str, bool, Exception]: ...
