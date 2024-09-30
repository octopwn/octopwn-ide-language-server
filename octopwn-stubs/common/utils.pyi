import datetime
import json
from _typeshed import Incomplete
from email.mime import base as base

def gts(td: datetime.datetime) -> int: ...
def gtt() -> datetime.datetime: ...
def don(x, default: str = '-'): ...
def ion(x, default: Incomplete | None = None): ...
def isint(x): ...
def isip(x) -> bool: ...
def isipnet(x) -> bool: ...
def convert_bool(x, default: bool = False): ...
def chunker(seq, size): ...
def hexdump(src: bytes, length: int = 16, sep: str = '.', offset: int = 0) -> str:
    """
\tPretty printing binary data blobs
\t:param src: Binary blob
\t:type src: bytearray
\t:param length: Size of data in each row
\t:type length: int
\t:param sep: Character to print when data byte is non-printable ASCII
\t:type sep: str(char)
\t:param offset: Start offset of the data to print
\t:type offset: int
\t:return: str
\t"""
def create_table(lines, separate_head: bool = True) -> str:
    """Creates a formatted table given a 2 dimensional array"""
def create_random_file(basename: Incomplete | None = None, ext: str = 'txt') -> str: ...
def create_random_filepath(basedir: Incomplete | None = None, basename: Incomplete | None = None, ext: str = 'txt') -> str: ...
def sizeof_fmt(num: float, suffix: str = 'B') -> str: ...
def get_table_help(table): ...

class UniversalEncoder(json.JSONEncoder):
    """
\tUsed to override the default json encoder to provide a direct serialization for formats
\tthat the default json encoder is incapable to serialize
\t"""
    def default(self, obj): ...

def create_server_ssl_context(cert_content, key_content, protocol=...):
    """
    Create an SSL context for a server using either file paths or direct string content.

    :param cert_content: Certificate file path or string content.
    :param key_content: Key file path or string content.
    :return: An SSL context.
    """
