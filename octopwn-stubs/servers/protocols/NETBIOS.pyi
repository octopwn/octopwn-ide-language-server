import enum
from _typeshed import Incomplete

class DNSResponseCode(enum.Enum):
    NOERR = 0
    FORMATERR = 1
    SERVERERR = 2
    NAMEERR = 3
    NOTIMPL = 4
    REFUSED = 5
    RESERVED6 = 6
    RESERVED7 = 7
    RESERVED8 = 8
    RESERVED9 = 9
    RESERVED10 = 10
    RESERVED11 = 11
    RESERVED12 = 12
    RESERVED13 = 13
    RESERVED14 = 14
    RESERVED15 = 15

class NBQType(enum.Enum):
    NB = 32
    NBSTAT = 33

class NBQClass(enum.Enum):
    IN = 1

class NBRType(enum.Enum):
    A = 1
    NS = 2
    NULL = 10
    NB = 32
    NBSTAT = 33

class NBRClass(enum.Enum):
    IN = 1

class NBTSNMFlags(enum.IntFlag):
    AUTHORATIVEANSWER = 64
    TRUNCATED = 32
    RECURSIONDESIRED = 16
    RECURSIONAVAILABLE = 8
    BROADCAST = 1

class NBTNSOpcode(enum.Enum):
    QUERY = 0
    REGISTRATION = 5
    RELEASE = 6
    WACK = 7
    REFRESH = 8

class NBTSResponse(enum.Enum):
    REQUEST = 0
    RESPONSE = 1

class NBTNSPacket:
    NAME_TRN_ID: Incomplete
    RESPONSE: Incomplete
    NM_FLAGS: Incomplete
    OPCPDE: Incomplete
    RCODE: Incomplete
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
    OPCODE: Incomplete
    def construct(self, TID, response, opcode, nmflags, rcode: int = 0, questions=[], answers=[], authorities=[], additionals=[]) -> None: ...
    def to_bytes(self): ...

class NBQuestion:
    QNAME: Incomplete
    QTYPE: Incomplete
    QCLASS: Incomplete
    def __init__(self) -> None: ...
    def from_bytes(bbuff): ...
    def from_buffer(buff): ...
    def to_bytes(self): ...
    def construct(self, qname, qtype, qclass) -> None: ...

class NBResource:
    NAME: Incomplete
    TYPE: Incomplete
    CLASS: Incomplete
    TTL: Incomplete
    RDLENGTH: Incomplete
    RDATA: Incomplete
    def __init__(self) -> None: ...
    def from_bytes(bbuff): ...
    def from_buffer(buff) -> None: ...
    def to_bytes(self): ...
    def construct(self, name, rtype, ip, flags: int = 0, ttl: int = 3000, rclass=...) -> None: ...

class NBSuffixGroup(enum.Enum):
    MACHINE_GROUP = 0
    MASTER_BROWSER = 1
    BROWSER_SERVICE = 30
    @classmethod
    def has_value(cls, value): ...

class NBSuffixUnique(enum.Enum):
    WORKSTATION = 0
    DOMAIN = 27
    MACHINE_GROUP = 29
    SERVER = 32
    DOMAIN_CONTROLLER = 28
    UNKNOWN_1 = 25
    UNKNOWN_2 = 72
    @classmethod
    def has_value(cls, value): ...

class NBName:
    length: Incomplete
    name: Incomplete
    suffix: Incomplete
    def __init__(self) -> None: ...
    def from_bytes(bbuff): ...
    def from_buffer(buff): ...
    def construct(name, suffix=...): ...
    def to_bytes(self): ...
    def encode_NS(name, suffix): ...
    def decode_NS(encoded_name): ...
