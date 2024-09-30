from _typeshed import Incomplete
from asyauth.common.constants import asyauthProtocol
from asysocks.unicomm.common.target import UniProto, UniTarget as UniTarget
from octopwn import logger as logger
from octopwn._version import __banner__ as __banner__
from octopwn.clients import OCTOPWN_CLIENT_TABLE as OCTOPWN_CLIENT_TABLE
from octopwn.clients.base import ClientConsoleBase as ClientConsoleBase
from octopwn.common.clientconfig import ClientConfig as ClientConfig, ClientConfigBase as ClientConfigBase, ScannerConfig as ScannerConfig, ServerConfig as ServerConfig, UtilsConfig as UtilsConfig
from octopwn.common.credential import Credential as Credential, OCTOPWN_CREDENTIALS_TSV_HDR as OCTOPWN_CREDENTIALS_TSV_HDR
from octopwn.common.licensing.client import LicensingException as LicensingException, OctoLicensingClient as OctoLicensingClient
from octopwn.common.proxy import Proxy as Proxy, ProxyChain as ProxyChain
from octopwn.common.screenhandler import ScreenHandlerBase as ScreenHandlerBase
from octopwn.common.target import Target as Target
from octopwn.common.utils import gts as gts, gtt as gtt, ion as ion
from octopwn.remote.protocol.python import messages_pb2 as messages_pb2, smb_pb2 as smb_pb2
from octopwn.servers import OCTOPWN_SERVER_TABLE as OCTOPWN_SERVER_TABLE
from octopwn.servers.wsnetws.console import WSNETServer as WSNETServer
from octopwn.utils import OCTOPWN_UTIL_TABLE as OCTOPWN_UTIL_TABLE
from typing import Any

class OctoPwn(ClientConsoleBase):
    prompt: str
    screen_handler: Incomplete
    work_dir: Incomplete
    session_dir: Incomplete
    periodic_save: Incomplete
    session_file: Incomplete
    restore_clients: Incomplete
    restore_clientmessages: Incomplete
    main_stopped_evt: Incomplete
    clients: Incomplete
    client_messages: Incomplete
    current_client_id: int
    client_msg_queue: Incomplete
    client_ctr: int
    default_timeout: int
    dcip: Incomplete
    realm: Incomplete
    resolver: Incomplete
    credentials: Incomplete
    targets: Incomplete
    proxies: Incomplete
    targets_checksum_lookup: Incomplete
    credentials_checksum_lookup: Incomplete
    current_credid: int
    current_targetid: int
    current_proxyid: int
    current_client_ctr: int
    scannertypes_hint: Incomplete
    clienttypes_hint: Incomplete
    utiltypes_hint: Incomplete
    supported_clients: Incomplete
    supported_scanners: Incomplete
    supported_servers: Incomplete
    supported_utils: Incomplete
    def __init__(self, screen_handler: ScreenHandlerBase, work_dir: str = None, periodic_save: bool = True, session_dir: str = None, licensing: OctoLicensingClient = None) -> None: ...
    def getscannerhints(self): ...
    def getclienthints(self): ...
    def getutilhints(self): ...
    def sanitize_path(self, x: str, to_raise: bool = False): ...
    def normalize_path(self, file_name: Incomplete | None = None): ...
    def get_plugin_script(self, pluginname): ...
    async def print(self, msg: str = '', h_username: Incomplete | None = None) -> None:
        """
\t\tthis is to hook the parent class' print.
\t\tshould only be used by this class
\t\t"""
    async def do_listop(self, to_print: bool = True, h_token: Incomplete | None = None):
        """Lists all pending operations on all sessions"""
    async def do_stop(self, cid: int, pid: int, to_print: bool = True):
        """Stops a pending operation on a given session"""
    def cwd(self, new_rootpath) -> None:
        """Changes the root directory (!not workdir!) It is useful for file downloads"""
    @staticmethod
    def load(filename, screen_handler: ScreenHandlerBase, work_dir: str = None, periodic_save: bool = True, session_dir: str = None, licensing: OctoLicensingClient = None): ...
    async def print_main_window(self, msg: str, username: Incomplete | None = None): ...
    def prettyclient(self, credid, targetid): ...
    async def do_winsetup(self, to_print: bool = True):
        """Automatically adds target and creds. (Windows only)
Please note that creds will only be useful when selecting SSPI-NTLM or SSPI-KERBEROS auth
"""
    def do_quit(self) -> None:
        """Exits application"""
    def do_save(self, sessionfilename: Incomplete | None = None, to_print: bool = True) -> None: ...
    def get_credid(self): ...
    def get_targetid(self): ...
    def get_proxyid(self): ...
    def get_clientid(self, force_cid: int = None): ...
    def get_client(self, client_id): ...
    async def do_changeworkdir(self, dirpath) -> None: ...
    async def do_refreshcreds(self, force: bool = False) -> None:
        """Refreshes the credentials window"""
    async def addcredential_obj(self, credential: Credential, to_print: bool = True): ...
    async def do_addcred(self, username_with_domain: str, secret: str, secrettype: str = 'password', certfile: str = None, keyfile: str = None):
        """Adds a new credential
WARINIG: special characters need to be correctly escaped!
You can double-check the correct value with the 'describe' command

Parameters:
  username_with_domain (str): Example: TEST\\\\Administrator
  secret (str)    : Authentication secret. Value depends on 'secrettype'
  secrettype (str): Type of secret specified in 'secret'. Dafult: password

Accepted values for 'secrettype':
  PASSWORD : the 'secret' is a plaintext password
  NT       : the 'secret' is an NT hash of a plaintext password
  RC4      : the 'secret' is an NT hash of a plaintext password
  AES(XXX) : the 'secret' is a long-term kerberos key of type AES.
             XXX can be omitted or '128' or '256'
  KEYTAB   : the 'secret' is a path to a .keytab file
  CCACHE   : the 'secret' is a path to a .ccache file
  PFX/P12  : the 'username_with_domain' is an alternative domain/user 
                 (if not needed, just use '' -empty string-)
             'secret' is the password for the file 
\t\t\t 'certfile' must be pointing to the .pem/.p12 file
  PEM:     : the 'username_with_domain' is an alternative domain/user 
                  (if not needed, just use '' -empty string-)
             'secret' is the password for the file 
             'certfile' must be pointing to the .pem file
             'keyfile' must be pointing to the .pem file
  CERTSTORE: -notyet- 
  
"""
    async def do_refreshtargets(self, force: bool = False) -> None:
        """Refreshes the targets window"""
    async def do_targetport(self, tid: int, port: int): ...
    async def addtarget_obj(self, target: Target, to_print: bool = True): ...
    async def do_addtarget(self, ip: str, port: int = None, dcip: str = None, realm: str = None, hostname: str = None, to_print: bool = True):
        """Adds a new target.
Warning! 'hostname' and 'dcip' is mandatory for kerberos authentication!

Parameters:
  ip (str): Type of the object to describe
  port (int): Port of the destination service. Optional.
  dcip (str): IP address of the Domain Controller. Optional.
  realm (str): Realm of the host. Optional
  hostname (str): Hostname of target. Preferably FQDN. Optional.
"""
    async def do_dcip(self, dcip: Incomplete | None = None, to_print: bool = True):
        """Gets or sets the IP address of the domain controller which will be used while adding targets"""
    async def do_realm(self, realm: Incomplete | None = None, to_print: bool = True):
        """Gets or sets the default realm which will be used while adding targets"""
    async def do_resolver(self, resolverid: Incomplete | None = None, to_print: bool = True):
        """Gets or sets the clientid of a DNS session which will be used when adding targets"""
    async def do_deltarget(self, tid):
        """Removes target from targets list"""
    async def do_delcred(self, tid):
        """Removes credential from credentials list"""
    async def do_settarget(self, targetid: int, param: str, value: Any, to_print: bool = True, to_refresh: bool = True):
        """Changes an arbitrary variable on the given target. 
This is useful to change parameters (especially the 'dcip') after target has been created.

Parameters:
  targetid (int): ID of the Target object to be changed
  param (str): Name of the variable of the Target object to be changed
  value (any): The updated value
"""
    async def do_refreshproxyies(self, force: bool = False) -> None:
        """Refreshes the proxy window"""
    async def do_refresh(self, force: bool = False) -> None: ...
    async def do_describe(self, cmd: str, tid: int, to_print: bool = True):
        """Prints data about the object (cred or target or proxy)
Parameters:
  cmd (str): Type of the object to describe
  tid (str): ID of the object to describe

Accepted values for 'cmd':
  CRED  : The 'tid' references a Credential object
  TARGET: The 'tid' references a Target object
  PROXY : The 'tid' references a Proxy or Proxychain object
"""
    async def addproxy_obj(self, proxy: Proxy, to_print: bool = True): ...
    async def do_addproxy(self, ptype: str, ip: str, port: int, agentid: str = None):
        """Adds a new proxy
Parameters:
  ptype   (str): Proxy protocol type
  ip      (str): IP of the proxy server
  port    (int): Port of the proxy server
  agentid (str): Agentid. Optional.

Accepted values for 'ptype':
  SOCKS5
  SOCKS4
  SOCKS4A
  HTTP
  HTTPS
  WSNET
  WSSNET
  WSNETWS
"""
    async def do_addproxychain(self, chainid: int, proxyid: int):
        """Adds a proxy to a proxy chain
Parameters:
  chainid (int): ID of the Proxychain object
  proxyid (int): ID of the Proxy to be added to the chain
"""
    async def do_createchain(self, description: str = None):
        """Creates a new Proxy chain"""
    async def do_refreshclients(self, force: bool = False):
        """Refreshes the clients window"""
    async def create_generic_scanner(self, scannertype: str, description: str = None, force_cid: int = None, final_type: str = 'SCANNER'): ...
    async def do_createscanner(self, scannertype: str, description: str = None, force_cid: int = None):
        """Creates a new scanner instance.
Parameters:
  scannertype (str): Scanner type

Accepted values for 'scannertype':
  SMBSESSION       : Enumerates SMB sessions on the target
  SMBPROTO         : SMB dialect and NTLM signing flags enum
  SMBPRINTNIGHTMARE: Checks if target is vulnerable to printnightmare
  SMBFINGER        : Scans targets for OS type and version
  SMBIFACE         : Enumerates all network interfaces on target
  SMBADMIN         : Tries to guess wether the user is admin on the targets
  SMBREGDUMP       : SMB remote registry secrets dumper
  SMBFILE          : Enumerates all shares/folders/files on targets
  RDPSCREEN        : RDP screenshot scanner
  RDPLOGIN         : RDP login scanner
  RDPCAP           : RDP capabilities scanner
  KRB5USER         : Kerberos user enumerator
  PORTSCAN         : Basic port scanner
  JACKDAW          : Full Domain enumeration
"""
    async def do_createserver(self, stype: str, description: str = None, force_cid: int = None):
        """Creates a new server instance.
Parameters:
  stype (str): Server type

Accepted values for 'ctype':
  LLMNR : LLMNR
  NBTNS : NBTNS
  MDNS  : MDNS

"""
    async def create_dummy_client(self, ctype: str, atype: str, credid: int, targetid: int, proxyid: int = None, description: str = None, force_cid: int = None):
        """Some objects cannot be reloaded because they tied to sockets/other dynamic content which is not serializable"""
    async def do_createutil(self, utype: str, description: str = None, force_cid: int = None, h_forcelocal: bool = False):
        """Creates a new utility instance.
Parameters:
  utype (str): Utility type

Accepted values for 'ctype':
  PYPYKATZ : LSASS/REGISTRY/NTDS parsing and cryptographic functions
  DPAPI    : Decryptor functions for DPAPI
  JACKDAW  : Jackdaw
  NMAP     : Nmap XML file parsing
  MASSCAN  : Masscan XML file parsing
  NOTES    : (GUI only) Markdown notes

"""
    async def do_getdescription(self, otype: str, oid: str, to_print: bool = True):
        """This is just for a test..."""
    async def do_changedescription(self, otype: str, oid: str, description: str):
        """Changes the description text for client/target/credential/proxy"""
    async def preprocess_client_params(self, ctype: str, atype: str, credid: int, targetid: int, proxyid: int = None, port: int = None, timeout: int = None): ...
    async def do_createclient(self, ctype: str, atype: str, credid: int, targetid: int, proxyid: int = None, description: str = None, port: int = None, timeout: int = None, force_cid: int = None):
        """Creates a new client of a specific type and authentication method. 
You must create at least one Credential and one Target before using this, 
Proxy is optional.

Parameters:
  ctype    (str): Client type
  atype    (str): Authentication type
  credid   (int): ID of the Credential which will be used for authentication
  targetid (int): ID of the Target which will be used to connect to.
  proxyid  (int): ID of the Proxy to be used to reach the target

Accepted values for 'ctype':
  SMB  : SMB client, defaults to SMB3 (on pyodide SMB2)
  SMB2 : SMB client which uses version 2 of the SMB protocol
  SMB3 : SMB client which uses version 3 of the SMB protocol
  SMBQ : SMB client which uses version 2 + connection layer is QUIC
  LDAP : LDAP client
  LDAPS: LDAP client which will use SSL/TLS
  KERBEROS: Kerberos client
  RDP: RDP client
  VNC: VNC client
  NC/NETCAT: Netcat TCP client

Accepted values for 'atype':
  Accepted values depends on the client type and the Credential used!
  For SMB:
    NTLM: Uses the NTLM authentication protocol.
        Compatible credential types:
          Password/NT/RC4
    KERBEROS: Uses the Kerberos authentication protocol.
        Compatible credential types:
          Password/NT/RC4/AES/AES128/AES256/PFX/CERTFILE/CERTSTORE/PEM/KEYTAB/CCACHE
    SSPI: Uses the integrated auth on Windos.

  For LDAP and LDAPS:
    SIMPLE: Uses plaintext auth method
        Compatible credential types:
          Password
    SICILY: Uses SICILY (old NTLM) auth method
        Compatible credential types:
          Password/NT/RC4
    NTLM: Uses the GSSAPI/NTLM authentication protocol.
        Compatible credential types:
          Password/NT/RC4
    KERBEROS: Uses the GSSAPI/Kerberos authentication protocol.
        Compatible credential types:
          Password/NT/RC4/AES/AES128/AES256/PFX/CERTFILE/CERTSTORE/PEM/KEYTAB/CCACHE
    SSPI: Uses the integrated auth on Windos.

  For Kerberos (standalone client):
        Compatible credential types:
          Password/NT/RC4/AES/AES128/AES256/PFX/CERTFILE/CERTSTORE/PEM/KEYTAB/CCACHE
  For RDP:
    Generic rule: for RDP you will need to have plaintext password.
    If not using Password then the client will attempt logging in via
    restricted mode, but this isn't always allowed

\tPLAIN: Uses the old RDP protocol with plaintext password
    NTLM: Uses the CREDSSP/NTLM authentication protocol.
        Compatible credential types:
          Password/NT/RC4
    KERBEROS: Uses the CREDSSP/Kerberos authentication protocol.
        Compatible credential types:
          Password/NT/RC4/AES/AES128/AES256/PFX/CERTFILE/CERTSTORE/PEM/KEYTAB/CCACHE
  For VNC:
    For VNC you will need to have plaintext password, or no password

\tPLAIN: Uses the DES based authentication as described in the RFC
\tNONE: Tries to authenticate without password
  For NetCat:
    NONE: must be set to none
"""
    async def do_netcat(self, targetid: int, port: int, proxyid: int = None, timeout: int = 10, description: str = None, force_cid: int = None): ...
    async def do_dnsclient(self, targetid: int, port: int = 53, proxyid: int = None, timeout: int = 10, description: str = None, force_cid: int = None): ...
    async def do_switchclient(self, client_id: int, to_print: bool = True):
        """Changes the current clinet INPUT and OUTPUT window to another one"""
    def get_ldap_factory(self, cid, tid, proto: UniProto = ..., authtype: asyauthProtocol = ..., pid: int = None, wsnetreuse: bool = True, timeout: int = 5):
        """Creates a valid LDAP factory object using the credential/target/proxy id and uth types supplied"""
    def get_rdp_factory_dummy(self, cid, iosettings, authtype: asyauthProtocol = ..., pid: Incomplete | None = None, wsnetreuse: bool = True, timeout: int = 5):
        """Retruns an SMB factory object with invalid target, but working credentials. This can act as a template for creating actual targets on-demand during scan"""
    def get_smb_factory_dummy(self, cid, authtype: asyauthProtocol = ..., pid: Incomplete | None = None, wsnetreuse: bool = True, timeout: int = 5):
        """Retruns an SMB factory object with invalid target, but working credentials. This can act as a template for creating actual targets on-demand during scan"""
    def get_smb_factory(self, cid: int, tid: int, authtype: asyauthProtocol = ..., pid: int = None, wsnetreuse: bool = True, timeout: int = 5):
        """Creates a valid SMB factory object using the credential/target/proxy id and uth types supplied"""
    def get_kerberos_factory(self, cid: int, tid: int, pid: int = None, wsnetreuse: bool = True, timeout: int = 5):
        """Creates a valid Kerberos url object using the credential/target/proxy id and uth types supplied"""
    async def do_winauto(self): ...
    async def do_wsnetauto(self):
        """Sets DC/realm and credential using WSNET"""
    async def add_wsnet_cred(self, domain, username): ...
    async def client_changeprompt_cb(self, client_id, newprompt) -> None: ...
    def input_handler(self, in_buffer, clientid: Incomplete | None = None, username: str = 'default'): ...
    async def print_session_message(self, client_id, msg, username) -> None: ...
    async def do_credexport(self, stype: str = None, fields: str = None):
        '''Exports credentials to file.
Param: stype
Param: fields
stype adds a filter to the secre-type fso only cretain secret formats will be exported
fields selects which values should be exported. This can be multiple fields separated by ",". Do not use spaces!
'''
    async def do_unzip(self, fname):
        """Extracts all files from a zipfile to a new folder in the workdir"""
    async def do_version(self):
        """Prints versions of internal packages"""
    async def do_remoteListDirectory(self, path: str, h_clientid, h_token): ...
    async def do_remoteDownloadFile(self, path: str, h_clientid: Incomplete | None = None, h_token: Incomplete | None = None): ...
    async def do_remotedeleteDirectory(self, path: str, h_clientid: Incomplete | None = None, h_token: Incomplete | None = None): ...
    async def do_remotecreateDirectory(self, path: str, h_clientid: Incomplete | None = None, h_token: Incomplete | None = None): ...
    async def do_remotedeleteFile(self, path: str, h_clientid: Incomplete | None = None, h_token: Incomplete | None = None): ...
    async def do_remotecreateFile(self, path: str, h_clientid: Incomplete | None = None, h_token: Incomplete | None = None): ...
    async def create_client_smb(self, ctype: str, authtype: str, credid: int, tid: int, pid: int, description: str = None, timeout: int = 10, port: int = 445, force_cid: int = None): ...
    async def create_client_dce(self, ctype: str, authtype: str, credid: int, tid: int, pid: int, description: str = None, timeout: int = 10, port: int = 445, force_cid: int = None): ...
    async def create_client_ldap(self, ctype: str, authtype: str, credid: int, tid: int, pid: int, description: str = None, timeout: int = 10, port: int = None, force_cid: int = None): ...
    async def create_client_kerberos(self, ctype: str, authtype: str, credid: int, tid: int, pid: int, description: str = None, timeout: int = 10, port: int = None, force_cid: int = None): ...
    async def create_client_rdp(self, ctype: str, authtype: str, credid: int, tid: int, pid: int, description: str = None, timeout: int = 10, port: int = None, force_cid: int = None): ...
    async def create_client_winrm(self, ctype: str, authtype: str, credid: int, tid: int, pid: int, description: str = None, timeout: int = 10, port: int = None, force_cid: int = None): ...
    async def create_client_ssh(self, ctype: str, authtype: str, credid: int, tid: int, pid: int, description: str = None, timeout: int = 10, port: int = None, force_cid: int = None): ...
    async def create_client_netcat(self, tid: int, port: int, pid: int, description: str = None, timeout: int = 10, force_cid: int = None): ...
    async def create_client_dns(self, tid: int, port: int, pid: int, description: str = None, timeout: int = 10, force_cid: int = None): ...
    async def create_client(self, clid, prompt, client_settings, client): ...
    async def do_report(self, include_passwords: bool = True): ...
    async def do_devtest(self): ...
    async def load_plugins(self, plugins: list[str], h_forcelocal: bool = False): ...
    async def send_info(self, motd: Incomplete | None = None) -> None: ...
    async def remote_message(self, msg_data: bytes, username: str, raddr: str, clientid: str, is_emscripten: bool = False): ...
    async def create_generic_client(self, ctype: str, atype: str, credid: int, targetid: int, proxyid: int = None, description: str = None, port: int = None, timeout: int = None, force_cid: int = None): ...
    async def run(self): ...
