from aiosmb.protocol.smb.message import *
from aiosmb.protocol.smb2.message import *
from _typeshed import Incomplete

class NetBIOSTransport:
    """
\tConverts incoming bytestream from the network starsport to SMB messages and vice-versa.
\tThis layer is presented so the network transport can be changed for a TCP/UDP/whatever type of transport.
\t"""
    network_transport: Incomplete
    socket_out_queue: Incomplete
    socket_in_queue: Incomplete
    in_queue: Incomplete
    out_queue: Incomplete
    outgoing_task: Incomplete
    incoming_task: Incomplete
    out_task_finished: Incomplete
    def __init__(self, network_transport) -> None: ...
    async def stop(self) -> None:
        """
\t\tStops the input output processing
\t\t"""
    async def run(self):
        """
\t\tStarts the input and output processing
\t\t"""
    async def handle_incoming_noparse(self) -> None:
        """
\t\tReads data bytes from the socket_in_queue and parses the NetBIOS messages and the SMBv1/2 messages.
\t\tDispatches the SMBv1/2 message objects.
\t\t"""
    async def handle_incoming(self) -> None:
        """
\t\tReads data bytes from the socket_in_queue and parses the NetBIOS messages and the SMBv1/2 messages.
\t\tDispatches the SMBv1/2 message objects.
\t\t"""
    async def handle_outgoing(self) -> None:
        """
\t\tReads SMBv1/2 outgoing message data bytes from out_queue, wraps them in NetBIOS object, then serializes them, then sends them to socket_out_queue
\t\t"""
