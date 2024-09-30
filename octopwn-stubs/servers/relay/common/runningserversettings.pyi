import asyncio
from _typeshed import Incomplete
from octopwn.servers.relay.common.authentication.spnego.relay import SPNEGORelay as SPNEGORelay
from octopwn.servers.relay.common.serversettings import ServerSettings as ServerSettings

class RunningServerSettings:
    server_settings: Incomplete
    gssapi: Incomplete
    log_q: Incomplete
    client_ip: Incomplete
    client_port: Incomplete
    def __init__(self, server_settings: ServerSettings, gssapi: SPNEGORelay, log_q: asyncio.Queue = None, client_ip: str = None, client_port: int = None) -> None: ...
