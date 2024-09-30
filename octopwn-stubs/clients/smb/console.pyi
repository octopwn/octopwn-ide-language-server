import asyncio
from _typeshed import Incomplete
from octopwn.clients.base import ClientConsoleBase as ClientConsoleBase
from octopwn.common.parsers.ntds import store_ntds_secrets as store_ntds_secrets
from octopwn.common.parsers.pfx import store_pfx_creds as store_pfx_creds
from octopwn.common.parsers.registry import store_registry_creds as store_registry_creds
from octopwn.common.utils import gts as gts, sizeof_fmt as sizeof_fmt
from octopwn.remote.protocol.python import messages_pb2 as messages_pb2, secrets_pb2 as secrets_pb2, smb_pb2 as smb_pb2

class SMBClient(ClientConsoleBase):
    machine: Incomplete
    is_anon: bool
    no_dce: bool
    shares: Incomplete
    def __init__(self, client_id, connection, cmd_q, msg_queue, prompt, octopwnobj) -> None: ...
    async def start(self): ...
    connection: Incomplete
    logon_ok: bool
    async def do_login(self):
        """Connect + login"""
    async def do_remoteShares(self, h_clientid: Incomplete | None = None, h_token: Incomplete | None = None): ...
    async def do_remoteListDirectory(self, path: str, h_clientid: Incomplete | None = None, h_token: Incomplete | None = None): ...
    async def do_remoteDownloadFile(self, path: str, h_clientid: Incomplete | None = None, h_token: Incomplete | None = None): ...
    async def do_remotedeleteDirectory(self, path: str, h_clientid: Incomplete | None = None, h_token: Incomplete | None = None): ...
    async def do_remotecreateDirectory(self, path: str, h_clientid: Incomplete | None = None, h_token: Incomplete | None = None): ...
    async def do_remotedeleteFile(self, path: str, h_clientid: Incomplete | None = None, h_token: Incomplete | None = None): ...
    async def do_remotecreateFile(self, path: str, h_clientid: Incomplete | None = None, h_token: Incomplete | None = None): ...
    async def listDirectory(self, path):
        """JS filebrowser helper"""
    async def deleteDirectory(self, path): ...
    async def createDirectory(self, path): ...
    async def downloadFile_inner(self, path: str, out_q: asyncio.Queue): ...
    async def downloadFile(self, path): ...
    async def deleteFile(self, path): ...
    async def do_logout(self):
        """Logs out from the current session, disconnects from the server"""
    async def do_nodce(self):
        """Disables automatic share listing on login"""
    async def do_shares(self, to_print: bool = True):
        """Lists available shares"""
    async def do_sessions(self, to_print: bool = True, h_token: Incomplete | None = None):
        """Lists sessions of connected users"""
    async def do_domains(self, to_print: bool = True, h_token: Incomplete | None = None):
        """Lists domain"""
    async def do_localgroups(self, to_print: bool = True, h_token: Incomplete | None = None):
        """Lists local groups"""
    async def do_domaingroups(self, domain_name, to_print: bool = True, h_token: Incomplete | None = None):
        """Lists groups in a domain"""
    async def do_groupmembers(self, domain_name, group_name, to_print: bool = True, h_token: Incomplete | None = None):
        """Lists members of an arbitrary group"""
    async def do_localgroupmembers(self, group_name, to_print: bool = True, h_token: Incomplete | None = None):
        """Lists members of a local group"""
    async def do_use(self, share_name):
        """selects share to be used"""
    async def do_dir(self):
        """Lists current directory contents"""
    async def do_ls(self):
        """Lists current directory contents"""
    async def do_refreshcurdir(self):
        """Refreshes file list in current directory"""
    async def do_cd(self, directory_name):
        """Change directory"""
    def get_current_shares(self): ...
    def get_current_dirs(self): ...
    def get_current_files(self): ...
    async def do_getfilesd(self, file_name):
        """Gets security descriptor for a file in the current directory"""
    async def do_getdirsd(self):
        """Gets security descriptor for current directory"""
    async def do_services(self, to_print: bool = True, h_token: Incomplete | None = None):
        """Lists remote services"""
    async def do_servicestart(self, service_name, to_print: bool = True):
        """Starts a remote service"""
    async def do_serviceen(self, service_name, to_print: bool = True):
        """Enables a remote service"""
    async def do_servicecreate(self, service_name, command, display_name: Incomplete | None = None, to_print: bool = True):
        """Creates a remote service"""
    async def do_servicecmdexec(self, command, timeout: int = 1, to_print: bool = True, h_token: Incomplete | None = None):
        """Executes a shell command as a service and returns the result"""
    async def do_servicedeploy(self, path_to_exec, remote_path, to_print: bool = True):
        """Deploys a binary file from the local system as a service on the remote system"""
    async def do_put(self, file_name):
        """Uploads a file to the remote share"""
    async def do_del(self, file_name):
        """Removes a file from the remote share"""
    async def do_regsave(self, hive_name, file_path):
        """Saves a registry hive to a file on remote share"""
    async def do_reglistusers(self, to_print: bool = True, h_token: Incomplete | None = None):
        """Lists users who have ever logged in to this machine"""
    async def do_get(self, file_name):
        """Download a file from the remote share to the current folder"""
    async def do_mkdir(self, directory_name):
        """Creates a directory on the remote share"""
    async def do_users(self, domain: Incomplete | None = None, to_print: bool = True, h_token: Incomplete | None = None):
        """List users in domain"""
    async def do_printerbug(self, attacker_ip, to_print: bool = True):
        """Printerbug"""
    async def do_tasks(self, to_print: bool = True, h_token: Incomplete | None = None):
        """List scheduled tasks """
    async def do_taskregister(self, template_file, task_name: Incomplete | None = None):
        """Registers a new scheduled task"""
    async def do_taskdel(self, task_name):
        """Deletes a scheduled task\t"""
    async def do_taskcmdexec(self, command, timeout: int = 2, to_print: bool = True, h_token: Incomplete | None = None) -> None:
        """Executes a shell command using the scheduled tasks service"""
    async def do_interfaces(self, to_print: bool = True, h_token: Incomplete | None = None):
        """Lists all network interfaces of the remote machine """
    async def do_enumall(self, depth: int = 3):
        """Enumerates all shares for all files and folders recursively """
    async def do_printerenumdrivers(self):
        """Enumerates all shares for all files and folders recursively """
    async def do_printnightmare(self, share, driverpath: str = ''):
        """printnightmare bug using the RPRN protocol """
    async def do_parprintnightmare(self, share, driverpath: str = ''):
        """printnightmare bug using the PAR protocol """
    async def do_lsassdump(self, method: str = 'service'):
        """Dumps LSASS remotely, parses it to extract secrets"""
    async def do_regdump(self, waittime: int = 5, to_print: bool = True, h_token: Incomplete | None = None):
        """Dumps remote registry hives, parses them remotely, extracts secrets"""
    async def do_dcsync(self, username: str = None, to_print: bool = True, h_token: int = None):
        """Dumps remote secrets using DCSync"""
    async def do_certreq(self, service, template, cn, altname):
        """Requests a new certificate for the user specified in CN with altname
service: name of the ADCS service
template: name of the certificate template to use
cn: CN of the user (in username@fqdn format like: victim@test.corp)
altname: Alternative user to be included in the cert (in username@fqdn format like: victim@test.corp) (optional)
"""
    async def do_certreqonbehalf(self, service, template, cn, altname, onbehalf, enroll_cert, enroll_password: Incomplete | None = None):
        """Requests a new certificate for the user specified in CN with altname on behalf of the user specified in onbehalf"""
    async def do_backupkeys(self):
        """Obtains the DPAPI domain backup keys"""
    async def do_cpasswd(self):
        """Searches SYSVOL for xml files containing cppasswords"""
