from _typeshed import Incomplete
from octopwn.clients.scannerbase import ScannerConsoleBase as ScannerConsoleBase

class PluginManagerUtil(ScannerConsoleBase):
    plugin_tasks: Incomplete
    plugin_ctr: Incomplete
    def __init__(self, client_id, connection, cmd_q, msg_queue, prompt, octopwnobj) -> None: ...
    async def customprint(self, msg) -> None: ...
    def get_plugin_name(self, pluginname): ...
    async def do_load(self, pluginname):
        """Loads and executes a plugin file. The plugin file must be in the plugins folder and must be named <pluginname>.py"""
