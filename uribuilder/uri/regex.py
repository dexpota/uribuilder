import re

# ABNF for URI

# scheme = ALPHA *( ALPHA / DIGIT / "+" / "-" / "." )
_SCHEME = r"[a-zA-Z][a-zA-Z0-9+.-]*"
SCHEME = re.compile(_SCHEME)

# port = *DIGIT
_PORT = r"[0-9]*"
PORT = re.compile(_PORT)

# unreserved = ALPHA / DIGIT / "-" / "." / "_" / "˜"
_UNRESERVED = r"[a-zA-Z0-9._~-]"
UNRESERVED = re.compile(_UNRESERVED)

# pct-encoded = "%" HEXDIG HEXDIG
_PCT_ENCODED = r"%[a-fA-F0-9]{2}"
PCT_ENCODED = re.compile(_PCT_ENCODED)
# sub-delims = "!" / "$" / "&" / "’" / "(" / ")" / "*" / "+" / "," / ";" / "="
_SUB_DELIMS = r"[!$&'()*+,;=]"
SUB_DELIMS = re.compile(_SUB_DELIMS)

# userinfo = *( unreserved / pct-encoded / sub-delims / ":" )
# ?: means a non-capturing group
_USERINFO = r"(?:{unreserved}|{pct_encoded}|{sub_delims})*".format(unreserved=_UNRESERVED,
                                                                   pct_encoded=_PCT_ENCODED,
                                                                   sub_delims=_SUB_DELIMS)
USERINFO = re.compile(_USERINFO)
# IP-literal = "[" ( IPv6address / IPvFuture ) "]"
# IPv4address = dec-octet "." dec-octet "." dec-octet "." dec-octet

# reg-name = *( unreserved / pct-encoded / sub-delims )
_REG_NAME = r"(?:{unreserved}|{pct_encoded}|{sub_delims})*".format(unreserved=_UNRESERVED,
                                                                   pct_encoded=_PCT_ENCODED,
                                                                   sub_delims=_SUB_DELIMS)
REG_NAME = re.compile(_REG_NAME)
# host = IP-literal / IPv4address / reg-name
# TODO do the full version
_HOST = _REG_NAME
HOST = re.compile(_HOST)

# authority = [ userinfo "@" ] host [ ":" port ]
_AUTHORITY = r"({userinfo}@)?{host}(:{port})?".format(
    userinfo=_USERINFO, host=_HOST, port=_PORT)
AUTHORITY = re.compile(_AUTHORITY)
# Definitions
# ALPHA: Upper- and lower-case ASCII letters (A–Z, a–z)
# DIGIT: Decimal digits (0–9)

# pchar = unreserved / pct-encoded / sub-delims / ":" / "@"
_PCHAR = r"(?:{unreserved}|{pct_encoded}|{sub_delims}|[:@])".format(unreserved=_UNRESERVED,
                                                                    pct_encoded=_PCT_ENCODED,
                                                                    sub_delims=_SUB_DELIMS)
PCHAR = re.compile(_PCHAR)
# segment = *pchar
_SEGMENT = r"{pchar}*".format(pchar=_PCHAR)
SEGMENT = re.compile(_SEGMENT)
# segment-nz = 1*pchar
_SEGMENT_NZ = r"{pchar}+".format(pchar=_PCHAR)
SEGMENT_NZ = re.compile(_SEGMENT_NZ)
# segment-nz-nc = 1*( unreserved / pct-encoded / sub-delims / "@" )
_SEGMENT_NZ_NC = r"{pchar}+".format(pchar=_PCHAR)
SEGMENT_NZ_NC = re.compile(_SEGMENT_NZ_NC)

_PATH_ABEMPTY = r"((?:/{segment})*)".format(segment=_SEGMENT)
PATH_ABEMPTY = re.compile(_PATH_ABEMPTY)
_PATH_ABSOLUTE = r"(/(?:{segment_nz}(?:/{segment})*)?)".format(segment=_SEGMENT,
                                                               segment_nz=_SEGMENT_NZ)
PATH_ABSOLUTE = re.compile(_PATH_ABSOLUTE)
_PATH_ROOTLESS = r"({segment_nz}(?:/{segment})*)".format(segment=_SEGMENT,
                                                         segment_nz=_SEGMENT_NZ)
PATH_ROOTLESS = re.compile(_PATH_ROOTLESS)
_PATH_EMPTY = r"()"
PATH_EMPTY = re.compile(_PATH_EMPTY)

# hier-part = "//" authority path-abempty / path-absolute / path-rootless / path-empty
_HIER_PART = r"//{authority}(?:{path_abempty}|{path_absolute}|{path_rootless}|{path_empty})".format(
    authority=_AUTHORITY, path_abempty=_PATH_ABEMPTY, path_absolute=_PATH_ABSOLUTE, path_rootless=_PATH_ROOTLESS,
    path_empty=_PATH_EMPTY)
HIER_PART = re.compile(_HIER_PART)
_FRAGMENT = r"((?:{pchar}|[/?])*)".format(pchar=_PCHAR)
FRAGMENT = re.compile(_FRAGMENT)
_QUERY = r"((?:{pchar}|[/?])*)".format(pchar=_PCHAR)
QUERY = re.compile(_QUERY)

# URI = scheme ":" hier-part [ "?" query ] [ "#" fragment ]
_URI = r"{scheme}:{hier_part}(\?{query})?(#{fragment})?".format(scheme=_SCHEME,
                                                                hier_part=_HIER_PART,
                                                                query=_QUERY,
                                                                fragment=_FRAGMENT)
URI = re.compile(_URI)
