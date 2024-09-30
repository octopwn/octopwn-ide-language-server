from _typeshed import Incomplete
from octopwn.core import OctoPwn as OctoPwn

class OctoPwnPluginBase:
    pluginname: Incomplete
    octopwnobj: Incomplete
    def __init__(self) -> None: ...
    async def print_exc(self, err: Exception, with_tb: bool = True, extra_msg: str = ''): ...
    async def print(self, msg) -> None: ...
    async def pluginsetup(self, pluginnname: str, octopwnobj: OctoPwn, print_cb): ...
    async def setup(self) -> None:
        """This function will be called when the plusing is initialized"""
    async def run(self) -> None:
        """Main entry point, add logic here"""
