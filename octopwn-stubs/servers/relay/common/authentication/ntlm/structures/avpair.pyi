import collections
import enum
from _typeshed import Incomplete

class MsvAvFlags(enum.IntFlag):
    CONSTRAINED_AUTH = 1
    MIC_PRESENT = 2
    SPN_UNTRUSTED = 4

class AVPAIRType(enum.Enum):
    MsvAvEOL = 0
    MsvAvNbComputerName = 1
    MsvAvNbDomainName = 2
    MsvAvDnsComputerName = 3
    MsvAvDnsDomainName = 4
    MsvAvDnsTreeName = 5
    MsvAvFlags = 6
    MsvAvTimestamp = 7
    MsvAvSingleHost = 8
    MsvAvTargetName = 9
    MsvChannelBindings = 10

class AVPairs(collections.UserDict):
    '''
\tAVPairs is a dictionary-like object that stores the "AVPair list" in a key -value format where key is an AVPAIRType object and value is the corresponding object defined by the MSDN documentation. Usually it\'s string but can be other object as well
\t'''
    def __init__(self, data: Incomplete | None = None) -> None: ...
    @staticmethod
    def from_bytes(bbuff): ...
    @staticmethod
    def from_buffer(buff): ...
    def to_bytes(self): ...

class AVPair:
    type: Incomplete
    data: Incomplete
    def __init__(self, data: Incomplete | None = None, type: Incomplete | None = None) -> None: ...
    def to_bytes(self): ...
