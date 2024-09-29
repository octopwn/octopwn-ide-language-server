from _typeshed import Incomplete
from octopwn._version import __version__ as __version__
from octopwn.clients.base import ClientConsoleBase as ClientConsoleBase
from octopwn.common.clientconfig import ClientConfig as ClientConfig, ClientConfigBase as ClientConfigBase, ScannerConfig as ScannerConfig, ServerConfig as ServerConfig, UtilsConfig as UtilsConfig
from octopwn.common.credential import Credential as Credential
from octopwn.common.proxy import Proxy as Proxy, ProxyChain as ProxyChain
from octopwn.common.target import Target as Target
from octopwn.core import OctoPwn as OctoPwn

class OctoPwnSessionFile:
    octopwnobj: Incomplete
    dcip: Incomplete
    realm: Incomplete
    resolver: Incomplete
    credentials: Incomplete
    targets: Incomplete
    proxies: Incomplete
    clients: Incomplete
    work_dir: Incomplete
    messagebuffers: Incomplete
    def __init__(self, octopwnobj: OctoPwn = None) -> None: ...
    def to_dict(self): ...
    def to_toml(self): ...
    @staticmethod
    def from_dict(d: dict): ...
    @staticmethod
    def from_toml(data: str): ...
