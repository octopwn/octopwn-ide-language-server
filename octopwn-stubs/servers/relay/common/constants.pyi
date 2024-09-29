import enum

class RELAYServerType(enum.Enum):
    SMB = 'SMB'
    HTTP = 'HTTP'
    LDAP = 'LDAP'

class RELAYClientType(enum.Enum):
    EXTENSION = 'EXTENSION'
    SMB = 'SMB'
    LDAP = 'LDAP'
    LDAPS = 'LDAPS'
    HTTP = 'HTTP'
    HTTPS = 'HTTPS'
    LSAD = 'LSAD'
    TSCH = 'TSCH'
    RSRV = 'RSRV'
    SRVS = 'SRVS'
    SAMR = 'SAMR'
    EVEN6 = 'EVEN6'
