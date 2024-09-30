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

class DNSType(enum.Enum):
    A = 1
    NS = 2
    MD = 3
    MF = 4
    CNAME = 5
    SOA = 6
    MB = 7
    MG = 8
    MR = 9
    NULL = 10
    WKS = 11
    PTR = 12
    HINFO = 13
    MINFO = 14
    MX = 15
    TXT = 16
    RP = 17
    AFSDB = 18
    SIG = 24
    KEY = 25
    AAAA = 28
    LOC = 29
    SRV = 33
    NAPTR = 35
    KX = 36
    CERT = 37
    DNAME = 39
    OPT = 41
    APL = 42
    DS = 43
    SSHFP = 44
    IPSECKEY = 45
    RRSIG = 46
    NSEC = 47
    DNSKEY = 48
    DHCID = 49
    NSEC3 = 50
    NSEC3PARAM = 51
    TLSA = 52
    HIP = 55
    CDS = 59
    CDNSKEY = 60
    OPENPGPKEY = 61
    TKEY = 249
    TSIG = 250
    IXFR = 251
    AXFR = 252
    ANY = 255
    URI = 256
    CAA = 257

class DNSClass(enum.Enum):
    IN = 1
    CS = 2
    CH = 3
    HS = 4
    ANY = 255

class DNSOpcode(enum.Enum):
    QUERY = 0
    IQUERY = 1
    STATUS = 2
    RESERVED3 = 3
    RESERVED4 = 4
    RESERVED5 = 5
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

class DNSFlags(enum.IntFlag):
    AA = 64
    TC = 32
    RD = 16
    RA = 8
    RESERVED1 = 4
    RESERVED2 = 2
    RESERVED3 = 1

class DNSResponse(enum.Enum):
    REQUEST = 0
    RESPONSE = 1

class DNSPacket:
    proto: Incomplete
    PACKETLEN: Incomplete
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
    def __init__(self, proto=...) -> None: ...
    async def from_streamreader(reader, proto=...): ...
    def from_bytes(bbuff, proto=...): ...
    def from_buffer(buff, proto=...): ...
    def to_bytes(self): ...
    def construct(TID, response, flags: int = 0, opcode=..., rcode=..., questions=[], answers=[], authorities=[], additionals=[], proto=...): ...

class DNSQuestion:
    QNAME: Incomplete
    QTYPE: Incomplete
    QCLASS: Incomplete
    QU: Incomplete
    def __init__(self) -> None: ...
    def from_bytes(bbuff): ...
    def from_buffer(buff): ...
    def to_bytes(self): ...
    def construct(qname, qtype, qclass, qu: bool = False): ...

class DNSOPT:
    Code: Incomplete
    Length: Incomplete
    Value: Incomplete
    size: Incomplete
    def __init__(self) -> None: ...
    def from_bytes(buff): ...
    def from_buffer(buff): ...

class DNSOPTResource:
    NAME: Incomplete
    TYPE: Incomplete
    UDPSIZE: Incomplete
    EXTRCODE: Incomplete
    VERSION: Incomplete
    DO: Incomplete
    Z: Incomplete
    RDLENGTH: Incomplete
    RDATA: Incomplete
    options: Incomplete
    def __init__(self) -> None: ...
    def from_bytes(bbuff): ...
    def from_buffer(buff): ...
    def to_bytes(self): ...

class DNSResource:
    NAME: Incomplete
    TYPE: Incomplete
    CLASS: Incomplete
    CFLUSH: Incomplete
    TTL: Incomplete
    RDLENGTH: Incomplete
    RDATA: Incomplete
    def __init__(self) -> None: ...
    def parse_header(self, buff) -> None: ...
    def from_bytes(bbuff): ...
    def from_buffer(buff): ...
    def to_bytes(self): ...
    def construct(self, rname, rtype, rdata, ttl: int = 30, rclass=..., cflush: bool = False): ...

class DNSAResource(DNSResource):
    ipaddress: Incomplete
    def __init__(self) -> None: ...
    def from_bytes(bbuff): ...
    def from_buffer(buff): ...
    def construct(rname, ipv4, ttl: int = 3000, rclass=..., cflush: bool = False): ...

class DNSAAAAResource(DNSResource):
    ipaddress: Incomplete
    def __init__(self) -> None: ...
    def from_bytes(bbuff): ...
    def from_buffer(buff): ...
    def construct(rname, ipv6, ttl: int = 3000, rclass=..., cflush: bool = False): ...

class DNSPTRResource(DNSResource):
    domainname: Incomplete
    def __init__(self) -> None: ...
    def from_bytes(bbuff): ...
    def from_buffer(buff): ...
    def construct(rname, domainname, ttl: int = 3000, rclass=..., cflush: bool = False): ...

class DNSSRVResource(DNSResource):
    Service: Incomplete
    Proto: Incomplete
    Name: Incomplete
    Priority: Incomplete
    Weight: Incomplete
    Port: Incomplete
    Target: Incomplete
    def __init__(self) -> None: ...
    def from_bytes(bbuff): ...
    def from_buffer(buff): ...

class DNSResourceParser:
    def from_bytes(bbuff): ...
    def from_buffer(buff): ...

class DNSName:
    name: str
    compressed: bool
    compressed_pos: Incomplete
    compressed_done: bool
    def __init__(self) -> None: ...
    def from_bytes(bbuff): ...
    def from_buffer(buff): ...
    def parse(self, data, rec: bool = False) -> None: ...
    def construct(name): ...
    def to_bytes(self): ...
