import enum
from _typeshed import Incomplete
from octopwn.servers.protocols.DNS import DNSQuestion as DNSQuestion, DNSResourceParser as DNSResourceParser, DNSResponseCode as DNSResponseCode

class LLMNRFlags(enum.IntFlag):
    CONFILCT = 64
    TRUNCATION = 32
    TENTATIVE = 16
    RESERVED1 = 8
    RESERVED2 = 4
    RESERVED3 = 2
    RESERVED4 = 1

class LLMNROpcode(enum.Enum):
    DEFAULT = 0

class LLMNRResponse(enum.Enum):
    REQUEST = 0
    RESPONSE = 1

class LLMNRPacket:
    TransactionID: Incomplete
    QR: Incomplete
    Opcode: Incomplete
    FLAGS: Incomplete
    Rcode: Incomplete
    QDCOUNT: Incomplete
    ANCOUNT: Incomplete
    NSCOUNT: Incomplete
    ARCOUNT: Incomplete
    Questions: Incomplete
    Answers: Incomplete
    Authorities: Incomplete
    Additionals: Incomplete
    def __init__(self) -> None: ...
    async def from_streamreader(reader): ...
    def from_bytes(bbuff): ...
    def from_buffer(buff): ...
    def to_bytes(self): ...
    def construct(TID, response, flags: int = 0, opcode=..., rcode=..., questions=[], answers=[], authorities=[], additionals=[]): ...
