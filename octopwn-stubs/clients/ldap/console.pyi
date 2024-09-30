from _typeshed import Incomplete
from msldap.connection import MSLDAPClientConnection as MSLDAPClientConnection
from msldap.ldap_objects import MSADMachine as MSADMachine, MSADUser as MSADUser
from msldap.protocol.constants import BASE as BASE, LEVEL as LEVEL
from octopwn.clients.base import ClientConsoleBase as ClientConsoleBase
from octopwn.common.credential import Credential as Credential
from octopwn.common.target import Target as Target
from octopwn.common.utils import UniversalEncoder as UniversalEncoder
from octopwn.remote.protocol.python import ldap_pb2 as ldap_pb2, messages_pb2 as messages_pb2
from winacl.dtyp.ace import ACCESS_DENIED_ACE as ACCESS_DENIED_ACE

class LDAPClient(ClientConsoleBase):
    adinfo: Incomplete
    ldapinfo: Incomplete
    domain_name: Incomplete
    client: Incomplete
    def __init__(self, client_id, connection: MSLDAPClientConnection, cmd_q, msg_queue, prompt, octopwnobj) -> None: ...
    async def start(self): ...
    connection: Incomplete
    logon_ok: bool
    async def do_login(self, to_print: bool = True, h_clientid: Incomplete | None = None, h_token: Incomplete | None = None):
        """Connect + login"""
    async def do_remoteListDirectory(self, path: str, h_clientid: Incomplete | None = None, h_token: Incomplete | None = None): ...
    async def listDirectory(self, path): ...
    async def do_logout(self):
        """Disconnect + logout"""
    async def do_ldapinfo(self, to_print: bool = True):
        """Prints detailed LDAP connection info (DSA)"""
    async def do_adinfo(self, show: bool = True, h_clientid: Incomplete | None = None, h_token: Incomplete | None = None):
        """Prints detailed Active Driectory info"""
    async def do_spns(self):
        """Fetches kerberoastable user accounts"""
    async def do_asrep(self):
        """Fetches ASREP-roastable user accounts"""
    async def do_computeraddr(self):
        """Fetches all computer accounts"""
    async def do_computeradd(self, computername: str = None, password: str = None):
        """Adds a new computer account"""
    async def do_changesamaccountname(self, dn: str, newname: str):
        """Changes the sAMAccountName of a given DN"""
    async def do_targetenum(self):
        """Grabs all computers in the domain and puts them in the targets window"""
    async def do_userenum(self, to_print: bool = False, h_token: Incomplete | None = None, h_clientid: Incomplete | None = None):
        """Grabs all computers in the domain and puts them in the targets window"""
    async def do_query(self, query, attributes: Incomplete | None = None):
        """Performs a raw LDAP query against the server.
Secondary parameter is the requested attributes SEPARATED WITH COMMA (,)"""
    async def do_tree(self, dn: Incomplete | None = None, level: int = 1):
        """Prints a tree from the given DN (if not set, the top) and with a given depth (default: 1)"""
    async def do_user(self, samaccountname):
        """Feteches a user object based on the sAMAccountName of the user"""
    async def do_machine(self, samaccountname):
        """Feteches a machine object based on the sAMAccountName of the machine"""
    async def do_schemaentry(self, cn):
        """Feteches a schema object entry object based on the DN of the object (must start with CN=)"""
    async def do_allschemaentry(self):
        """Feteches all schema object entry objects"""
    async def do_changeowner(self, new_owner_sid, target_dn, target_attribute: Incomplete | None = None):
        """Changes the owner in a Security Descriptor to the new_owner_sid on an LDAP object or on an LDAP object's attribute identified by target_dn and target_attribute. target_attribute can be omitted to change the target_dn's SD's owner"""
    async def do_addprivdcsync(self, user_dn, forest: Incomplete | None = None):
        """Adds DCSync rights to the given user by modifying the forest's Security Descriptor to add GetChanges and GetChangesAll ACE"""
    async def do_addprivaddmember(self, user_dn, group_dn):
        """Adds AddMember rights to the user on the group specified by group_dn"""
    async def do_setsd(self, target_dn, sddl):
        """Updates the security descriptor of an object"""
    async def do_getsd(self, dn):
        """Feteches security info for a given DN"""
    async def do_gpos(self):
        """Feteches security info for a given DN"""
    async def do_laps(self):
        """Feteches all laps passwords"""
    async def do_newlaps(self):
        """Feteches all Windows LAPS passwords"""
    async def do_groups_r(self, h_token: Incomplete | None = None, h_clientid: Incomplete | None = None): ...
    async def do_memberedges_r(self, h_token: Incomplete | None = None, h_clientid: Incomplete | None = None): ...
    async def do_groupmembership(self, dn):
        """Feteches names all groupnames the user is a member of for a given DN"""
    async def do_bindtree(self, newtree) -> None:
        """Changes the LDAP TREE for future queries. 
\t\t\t\t MUST be DN format eg. 'DC=test,DC=corp'
\t\t\t\t !DANGER! Switching tree to a tree outside of the domain will trigger a connection to that domain, leaking credentials!"""
    async def do_trusts(self):
        """Feteches domain trusts"""
    async def do_adduser(self, user_dn, password):
        """Creates a new domain user with password"""
    async def do_deluser(self, user_dn):
        """Deletes the user! This action is irrecoverable (actually domain admins can do that but probably will shout with you)"""
    async def do_changeuserpw(self, user_dn, newpass, oldpass: Incomplete | None = None):
        """Changes user password, if you are admin then old pw doesnt need to be supplied"""
    async def do_unlockuser(self, user_dn):
        """Unlock user by setting lockoutTime to 0"""
    async def do_enableuser(self, user_dn):
        """Unlock user by flipping useraccountcontrol bits"""
    async def do_disableuser(self, user_dn):
        """Unlock user by flipping useraccountcontrol bits"""
    async def do_addspn(self, user_dn, spn):
        """Adds an SPN entry to the users account"""
    async def do_delspn(self, user_dn, spn):
        """Removes an SPN entry to the users account"""
    async def do_addhostname(self, user_dn, hostname):
        """Adds additional hostname to computer account"""
    async def do_addusertogroup(self, user_dn, group_dn):
        """Adds user to specified group. Both user and group must be in DN format!"""
    async def do_deluserfromgroup(self, user_dn, group_dn):
        """Removes user from specified group. Both user and group must be in DN format!"""
    async def do_whoamisimple(self):
        """Simple whoami"""
    async def do_whoami(self):
        """Whoami"""
    async def do_rootcas(self, to_print: bool = True):
        """Lists Root CA certificates"""
    async def do_ntcas(self, to_print: bool = True):
        """Lists NT CA certificates"""
    async def do_aiacas(self, to_print: bool = True):
        """Lists AIA CA certificates"""
    async def do_enrollmentservices(self, to_print: bool = True):
        """Lists AIA CA certificates"""
    async def do_addcerttemplatenameflagaltname(self, certtemplatename, flags: Incomplete | None = None):
        """Modifyies the msPKI-Certificate-Name-Flag value of the specified certificate template and enables ENROLLEE_SUPPLIES_SUBJECT_ALT_NAME bit. If 'flags' is present then it will assign that value."""
    async def do_addenrollmentright(self, certtemplatename, user_dn):
        """Grants enrollment rights to a user (by DN) for the specified certificate template."""
    async def do_certtemplates(self, name: Incomplete | None = None, to_print: bool = True):
        """Lists certificate templates"""
    async def do_groupmembers(self, dn, recursive: bool = True, to_print: bool = True):
        """Returns all member users in a group specified by DN"""
    async def do_sid2dn(self, sid, to_print: bool = True):
        """Returns the DN for a given SID"""
    async def do_dn2sid(self, dn, to_print: bool = True):
        """Returns the SID for a given DN"""
    async def do_sam2dn(self, sAMAccountName, to_print: bool = True):
        """Fetches the DN of an object based on the sAMAccountName"""
    async def do_dn2sam(self, dn, to_print: bool = True):
        """Fetches the sAMAccountName of an object based on the DN"""
    async def do_sidresolv(self, sid, to_print: bool = True):
        """Returns the domain and username for a given SID"""
    async def do_certify(self, cmd: Incomplete | None = None, username: Incomplete | None = None):
        """Identifies all/vulnerable certificate templates (depending on cmd)."""
    async def do_gmsa(self, to_print: bool = True):
        """Lists all managed service accounts (MSA). If user has permissions it retrieves the password as well"""
    async def do_unconstrained(self):
        """Lists all unconstrained delegation objects"""
    async def do_constrained(self):
        """Lists all constrained delegation objects"""
    async def do_s4u2proxy(self):
        """Lists all S4U2Proxy objects"""
    async def do_dadms(self):
        """Lists all members of the domain administrators group"""
    async def do_dnszones(self, to_print: bool = True):
        """Lists all DNS zones"""
    async def do_dnsdump(self, zone: str = None):
        """Enumerates all DNS records and writes them in a file"""
    async def do_pre2000(self, to_print: bool = True):
        """Lists potentially abusable machine accounts created with pre windows-2000 flag"""
    async def do_addallowedtoactonbehalfofotheridentity(self, target_dn: str, other_identity_sid: str):
        """Adds a SID to the msDS-AllowedToActOnBehalfOfOtherIdentity protperty of target_dn"""
    async def do_modify(self, dn, attribute, value):
        """Modify an attribute of object. Only works with string data types!"""
    async def do_dump(self):
        """Fetches ALL user and machine accounts from the domain with a LOT of attributes"""
    async def do_fulldump(self):
        """Fetches user,computer,dns,groups,containers,ous,domains,trusts,spns"""
    async def do_bloodhound(self): ...
