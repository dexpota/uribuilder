# ABNF for URI

# scheme = ALPHA *( ALPHA / DIGIT / "+" / "-" / "." )
SCHEME = r"[a-zA-Z][a-zA-Z0-9+.-]*"

# port = *DIGIT
PORT = r"[0-9]*"

# unreserved = ALPHA / DIGIT / "-" / "." / "_" / "˜"
UNRESERVED = r"[a-zA-Z0-9._~-]"
# pct-encoded = "%" HEXDIG HEXDIG
PCT_ENCODED = r"%[a-fA-F0-9]{2}"
# sub-delims = "!" / "$" / "&" / "’" / "(" / ")" / "*" / "+" / "," / ";" / "="
SUB_DELIMS = r"[!$&'()*+,;=]"

# userinfo = *( unreserved / pct-encoded / sub-delims / ":" )
# ?: means a non-capturing group
USERINFO = r"(?:{unreserved}|{pct_encoded}|{sub_delims})*".format(unreserved=UNRESERVED,
                                                                  pct_encoded=PCT_ENCODED,
                                                                  sub_delims=SUB_DELIMS)
# IP-literal = "[" ( IPv6address / IPvFuture ) "]"
# IPv4address = dec-octet "." dec-octet "." dec-octet "." dec-octet

# reg-name = *( unreserved / pct-encoded / sub-delims )
REG_NAME = r"(?:{unreserved}|{pct_encoded}|{sub_delims})*".format(unreserved=UNRESERVED,
                                                                  pct_encoded=PCT_ENCODED,
                                                                  sub_delims=SUB_DELIMS)

# host = IP-literal / IPv4address / reg-name
# TODO do the full version
HOST = REG_NAME

# authority = [ userinfo "@" ] host [ ":" port ]
AUTHORITY = r"({userinfo}@)?{host}(:{port})?".format(userinfo=USERINFO, host=HOST, port=PORT)

# Definitions
# ALPHA: Upper- and lower-case ASCII letters (A–Z, a–z)
# DIGIT: Decimal digits (0–9)

# pchar = unreserved / pct-encoded / sub-delims / ":" / "@"
PCHAR = r"(?:{unreserved}|{pct_encoded}|{sub_delims}|[:@])".format(unreserved=UNRESERVED,
                                                                  pct_encoded=PCT_ENCODED,
                                                                  sub_delims=SUB_DELIMS)
# segment = *pchar
SEGMENT = r"{pchar}*".format(pchar=PCHAR)
# segment-nz = 1*pchar
SEGMENT_NZ = r"{pchar}+".format(pchar=PCHAR)
# segment-nz-nc = 1*( unreserved / pct-encoded / sub-delims / "@" )
SEGMENT_NZ_NC = r"{pchar}+".format(pchar=PCHAR)


PATH_ABEMPTY = r"((?:/{segment})*)".format(segment=SEGMENT)
PATH_ABSOLUTE = r"(/(?:{segment_nz}(?:/{segment})*)?)".format(segment=SEGMENT,
                                                             segment_nz=SEGMENT_NZ)
PATH_ROOTLESS = r"({segment_nz}(?:/{segment})*)".format(segment=SEGMENT,
                                                       segment_nz=SEGMENT_NZ)
PATH_EMPTY = r"()"

# hier-part = "//" authority path-abempty / path-absolute / path-rootless / path-empty
HIER_PART = r"//{authority}(?:{path_abempty}|{path_absolute}|{path_rootless}|{path_empty})".format(
    authority=AUTHORITY, path_abempty=PATH_ABEMPTY, path_absolute=PATH_ABSOLUTE, path_rootless=PATH_ROOTLESS,
    path_empty=PATH_EMPTY)

FRAGMENT = r"((?:{pchar}|[/?])*)".format(pchar=PCHAR)
QUERY = r"((?:{pchar}|[/?])*)".format(pchar=PCHAR)

# URI = scheme ":" hier-part [ "?" query ] [ "#" fragment ]
URI = r"{scheme}:{hier_part}(\?{query})?(#{fragment})?".format(scheme=SCHEME,
                                                              hier_part=HIER_PART,
                                                              query=QUERY,
                                                              fragment=FRAGMENT)
