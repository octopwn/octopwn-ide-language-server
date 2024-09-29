from _typeshed import Incomplete

class ClientConfigBase:
    config_type: Incomplete
    clientname: Incomplete
    completer: Incomplete
    description: Incomplete
    def __init__(self, config_type: str, clientname: str, completer, description: Incomplete | None = None) -> None: ...
    def to_dict(self) -> None: ...

class ClientConfig(ClientConfigBase):
    connection_type: Incomplete
    authentication_type: Incomplete
    target_id: Incomplete
    credential_id: Incomplete
    proxy_id: Incomplete
    client_type: Incomplete
    params: Incomplete
    port: Incomplete
    timeout: Incomplete
    def __init__(self, connection_type: str, authentication_type: str, target_id: int, credential_id: int, proxy_id: int, clientname: str, completer, client_type, description: Incomplete | None = None, params: Incomplete | None = None, port: int = None, timeout: int = None) -> None: ...
    def to_dict(self): ...
    @staticmethod
    def from_dict(d: dict): ...

class ScannerConfig(ClientConfigBase):
    scanner_type: Incomplete
    params: Incomplete
    def __init__(self, scanner_type: str, clientname, completer, description: Incomplete | None = None) -> None: ...
    def to_dict(self): ...
    @staticmethod
    def from_dict(d: dict): ...

class ServerConfig(ClientConfigBase):
    scanner_type: Incomplete
    params: Incomplete
    def __init__(self, scanner_type: str, clientname: str, completer, description: str = None) -> None: ...
    def to_dict(self): ...
    @staticmethod
    def from_dict(d: dict): ...

class UtilsConfig(ClientConfigBase):
    scanner_type: Incomplete
    params: Incomplete
    def __init__(self, scanner_type: str, clientname: str, completer, description: str = None) -> None: ...
    def to_dict(self): ...
    @staticmethod
    def from_dict(d: dict): ...
