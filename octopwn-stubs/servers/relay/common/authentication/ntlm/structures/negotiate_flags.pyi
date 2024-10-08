import enum
from _typeshed import Incomplete

class NegotiateFlags(enum.IntFlag):
    NEGOTIATE_56 = 2147483648
    NEGOTIATE_KEY_EXCH = 1073741824
    NEGOTIATE_128 = 536870912
    r1 = 268435456
    r2 = 134217728
    r3 = 67108864
    NEGOTIATE_VERSION = 33554432
    r4 = 16777216
    NEGOTIATE_TARGET_INFO = 8388608
    REQUEST_NON_NT_SESSION_KEY = 4194304
    r5 = 2097152
    NEGOTIATE_IDENTIFY = 1048576
    NEGOTIATE_EXTENDED_SESSIONSECURITY = 524288
    r6 = 262144
    TARGET_TYPE_SERVER = 131072
    TARGET_TYPE_DOMAIN = 65536
    NEGOTIATE_ALWAYS_SIGN = 32768
    r7 = 16384
    NEGOTIATE_OEM_WORKSTATION_SUPPLIED = 8192
    NEGOTIATE_OEM_DOMAIN_SUPPLIED = 4096
    J = 2048
    r8 = 1024
    NEGOTIATE_NTLM = 512
    r9 = 256
    NEGOTIATE_LM_KEY = 128
    NEGOTIATE_DATAGRAM = 64
    NEGOTIATE_SEAL = 32
    NEGOTIATE_SIGN = 16
    r10 = 8
    REQUEST_TARGET = 4
    NTLM_NEGOTIATE_OEM = 2
    NEGOTIATE_UNICODE = 1

NegotiateFlagExp: Incomplete
