from uribuilder.uri import HIER_PART, URI, SCHEME, QUERY
import re


def test_scheme():
    reg_expression = re.compile(SCHEME)
    assert reg_expression.match("http")


def test_query():
    reg_expression = re.compile(QUERY)
    assert reg_expression.match("a=1&b=1")


def test_hier_part_regex():
    reg_expression = re.compile(HIER_PART)
    assert reg_expression.match("//www.google.it/")
    assert reg_expression.match("//foo.com/blah_blah")


def test_valid_uri():
    reg_expression = re.compile(URI)
    assert reg_expression.match("http://foo.com/blah_blah")
    assert reg_expression.match("http://foo.com/blah_blah/")
    assert reg_expression.match("http://foo.com/blah_blah_(wikipedia)")
    assert reg_expression.match("http://foo.com/blah_blah_(wikipedia)_(again)")
    assert reg_expression.match("http://www.example.com/wpstyle/?p=364")
    assert reg_expression.match("https://www.example.com/foo/?bar=baz&inga=42&quux")
    assert reg_expression.match("http://✪df.ws/123")
    assert reg_expression.match("http://userid:password@example.com:8080")
    assert reg_expression.match("http://userid:password@example.com:8080/")
    assert reg_expression.match("http://userid@example.com")
    assert reg_expression.match("http://userid@example.com/")
    assert reg_expression.match("http://userid@example.com:8080")
    assert reg_expression.match("http://userid@example.com:8080/")
    assert reg_expression.match("http://userid:password@example.com")
    assert reg_expression.match("http://userid:password@example.com/")
    assert reg_expression.match("http://142.42.1.1/")
    assert reg_expression.match("http://142.42.1.1:8080/")
    assert reg_expression.match("http://➡.ws/䨹")
    assert reg_expression.match("http://⌘.ws")
    assert reg_expression.match("http://⌘.ws")
    assert reg_expression.match("http://foo.com/blah_(wikipedia)#cite-1")
    assert reg_expression.match("http://foo.com/blah_(wikipedia)_blah#cite-1")
    assert reg_expression.match("http://foo.com/unicode_(✪)_in_parens")
    assert reg_expression.match("http://foo.com/(something)?after=parens")
    assert reg_expression.match("http://☺.damowmow.com/")
    assert reg_expression.match("http://code.google.com/events/#&product=browser")
    assert reg_expression.match("http://j.mp")
    assert reg_expression.match("ftp://foo.bar/baz")
    assert reg_expression.match("http://foo.bar/?q=Test%20URL-encoded%20stuff")
    assert reg_expression.match("http://مثال.إختبار")
    assert reg_expression.match("http://例子.测试")
    assert reg_expression.match("http://उदाहरण.परीक्षा")
    assert reg_expression.match("http://-.~_!$&'()*+,;=:%40:80%2f::::::@example.com")
    assert reg_expression.match("http://1337.net")
    assert reg_expression.match("http://a.b-c.de")
    assert reg_expression.match("http://223.255.255.254")
    assert reg_expression.match("https://foo_bar.example.com/")