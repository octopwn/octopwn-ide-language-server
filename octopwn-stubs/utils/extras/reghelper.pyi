from _typeshed import Incomplete
from aiowinreg import logger as logger

class RegHelper:
    filepath: Incomplete
    filename: Incomplete
    filehandle: Incomplete
    hive: Incomplete
    def __init__(self, filepath) -> None: ...
    async def do_walk(self, path, depth: int = 2): ...
