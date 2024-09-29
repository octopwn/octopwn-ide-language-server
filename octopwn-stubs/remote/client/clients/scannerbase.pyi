from _typeshed import Incomplete
from octopwn.common.paramsutil import deserializeParamsDict as deserializeParamsDict, serializeParamsDict as serializeParamsDict
from octopwn.remote.client.clients.base import ClientConsoleBaseRemote as ClientConsoleBaseRemote
from octopwn.remote.protocol.python import messages_pb2 as messages_pb2

class ScannerConsoleBaseRemote(ClientConsoleBaseRemote):
    prompt: str
    params: Incomplete
    def __init__(self, octopwnobj, clientid, commands=[], command_modifier: Incomplete | None = None) -> None: ...
    async def process_message_internal(self, cmd) -> None: ...
