from _typeshed import Incomplete
from octopwn.remote.client.clients.base import ClientConsoleBaseRemote as ClientConsoleBaseRemote
from octopwn.remote.protocol.python import messages_pb2 as messages_pb2, smb_pb2 as smb_pb2

class SMBClientConsoleRemote(ClientConsoleBaseRemote):
    shares: Incomplete
    def __init__(self, octopwnobj, clientid, commands=[]) -> None: ...
    async def do_shares(self, to_print: bool = False): ...
    async def listDirectory(self, path: str): ...
    async def downloadFile_internal(self, token, res_q) -> None: ...
    async def downloadFile(self, path: str): ...
    async def deleteDirectory(self, path): ...
    async def createDirectory(self, path): ...
    async def deleteFile(self, path): ...
    async def createFile(self, localpath: str, remotepath: str): ...
    async def createFileBytes(self, remotepath, filedata): ...
