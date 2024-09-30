import enum
from _typeshed import Incomplete

class NTLMRevisionCurrent(enum.Enum):
    NTLMSSP_REVISION_W2K3 = 15
    NTLMSSP_REVISION_UNK = 255

class WindowsMajorVersion(enum.Enum):
    WINDOWS_MAJOR_VERSION_UNK = 255
    WINDOWS_MAJOR_VERSION_5 = 5
    WINDOWS_MAJOR_VERSION_6 = 6
    WINDOWS_MAJOR_VERSION_10 = 10

class WindowsMinorVersion(enum.Enum):
    WINDOWS_MINOR_VERSION_UNK = 255
    WINDOWS_MINOR_VERSION_0 = 0
    WINDOWS_MINOR_VERSION_1 = 1
    WINDOWS_MINOR_VERSION_2 = 2
    WINDOWS_MINOR_VERSION_3 = 3

WindowsProduct: Incomplete

class Version:
    ProductMajorVersion: Incomplete
    ProductMinorVersion: Incomplete
    ProductBuild: Incomplete
    Reserved: int
    NTLMRevisionCurrent: Incomplete
    WindowsProduct: Incomplete
    def __init__(self) -> None: ...
    @staticmethod
    def construct(major=..., minor=..., build: int = 1555): ...
    def to_bytes(self): ...
    @staticmethod
    def from_bytes(bbuff): ...
    @staticmethod
    def from_buffer(buff): ...
