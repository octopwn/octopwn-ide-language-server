from aiosmb.commons.exceptions import *
from aiosmb.protocol.smb.commands import *
from aiosmb.protocol.smb2.commands import *
from aiosmb.protocol.smb2.headers import *
from aiosmb.protocol.smb2.command_codes import *
from aiosmb.protocol.common import *
from aiosmb.wintypes.dtyp.constrcuted_security.guid import *
import enum
from _typeshed import Incomplete
from octopwn.servers.relay.common.authentication.spnego.relay import SPNEGORelay as SPNEGORelay
from octopwn.servers.relay.common.serversettings import ServerSettings as ServerSettings
from octopwn.servers.relay.smbrelay.protocol.netbios import NetBIOSTransport as NetBIOSTransport

class SMBConnectionStatus(enum.Enum):
    NEGOTIATING = 'NEGOTIATING'
    SESSIONSETUP = 'SESSIONSETUP'
    RUNNING = 'RUNNING'
    CLOSED = 'CLOSED'

class SMBConnectionSettings:
    client_ip: Incomplete
    client_port: Incomplete
    gssapi: Incomplete
    async_print_cb: Incomplete
    preferred_dialects: Incomplete
    MaxTransactSize: int
    MaxReadSize: int
    MaxWriteSize: int
    ServerGuid: Incomplete
    RequireSigning: bool
    def __init__(self, client_ip: str, client_port: int, gssapi: SPNEGORelay, async_print_cb) -> None: ...

class SMBServerConnection:
    client_ip: Incomplete
    client_port: Incomplete
    settings: Incomplete
    gssapi: Incomplete
    supported_dialects: Incomplete
    transport: Incomplete
    incoming_task: Incomplete
    keepalive_task: Incomplete
    activity_at: Incomplete
    selected_dialect: Incomplete
    signing_required: Incomplete
    encryption_required: bool
    last_treeid: int
    status: Incomplete
    OutstandingResponsesEvent: Incomplete
    OutstandingRequests: Incomplete
    OutstandingResponses: Incomplete
    pending_table: Incomplete
    TreeConnectTable_id: Incomplete
    TreeConnectTable_share: Incomplete
    FileHandleTable: Incomplete
    SequenceWindow: int
    MaxTransactSize: Incomplete
    MaxReadSize: Incomplete
    MaxWriteSize: Incomplete
    ServerGuid: Incomplete
    ClientGUID: Incomplete
    SupportsFileLeasing: bool
    SupportsMultiCredit: bool
    SupportsDirectoryLeasing: bool
    SupportsMultiChannel: bool
    SupportsPersistentHandles: bool
    SupportsEncryption: bool
    ClientCapabilities: int
    ServerCapabilities: Incomplete
    ClientSecurityMode: int
    ServerSecurityMode: Incomplete
    SessionId: int
    SessionKey: Incomplete
    SigningKey: Incomplete
    ApplicationKey: Incomplete
    EncryptionKey: Incomplete
    DecryptionKey: Incomplete
    session_closed: bool
    def __init__(self, settings: SMBConnectionSettings, transport: NetBIOSTransport) -> None: ...
    def get_extra_info(self): ...
    async def log_async(self, level, msg) -> None: ...
    async def disconnect(self) -> None: ...
    handle_in_task: Incomplete
    async def run(self) -> None: ...
    async def negotiate(self, req): ...
    async def session_setup(self, msg): ...
    async def recvSMB(self, message_id, ret_data: bool = False):
        """
\t\tReturns an SMB message from the outstandingresponse dict, OR waits until the expected message_id appears.
\t\t"""
    async def sendSMB(self, msg, ret_message: bool = False, compression_cb: Incomplete | None = None):
        """
\t\tSends an SMB message to teh remote endpoint.
\t\tmsg: SMB2Message or SMBMessage
\t\tReturns: MessageId integer
\t\t"""
