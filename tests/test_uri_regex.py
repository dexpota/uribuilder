from uribuilder.uri import HIER_PART
import re


def test_path_regex():
    reg_expression = re.compile(HIER_PART)
    assert reg_expression.match("//www.google.it/")
