from _typeshed import Incomplete
from octopwn.common.credential import Credential as Credential
from octopwn.remote.protocol.python import secrets_pb2 as secrets_pb2

async def store_ntds_secrets(mainobj, secret, to_print: bool = True, fileh: Incomplete | None = None) -> None: ...
