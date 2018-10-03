from uribuilder.uri import HIER_PART, URI, SCHEME, QUERY


def test_scheme():
    assert SCHEME.match("http")


def test_query():
    assert QUERY.match("a=1&b=1")


def test_hier_part_regex():
    assert HIER_PART.match("//www.google.it/")
    assert HIER_PART.match("//foo.com/blah_blah")


def test_valid_uri():
    assert URI.match("http://foo.com:/blah_blah")  # Test without port, only :
    assert URI.match("http://foo.com/blah_blah")
    assert URI.match("http://foo.com/blah_blah/")
    assert URI.match("http://foo.com/blah_blah_(wikipedia)")
    assert URI.match("http://foo.com/blah_blah_(wikipedia)_(again)")
    assert URI.match("http://www.example.com/wpstyle/?p=364")
    assert URI.match("https://www.example.com/foo/?bar=baz&inga=42&quux")
    assert URI.match("http://✪df.ws/123")
    assert URI.match("http://userid:password@example.com:8080")
    assert URI.match("http://userid:password@example.com:8080/")
    assert URI.match("http://userid@example.com")
    assert URI.match("http://userid@example.com/")
    assert URI.match("http://userid@example.com:8080")
    assert URI.match("http://userid@example.com:8080/")
    assert URI.match("http://userid:password@example.com")
    assert URI.match("http://userid:password@example.com/")
    assert URI.match("http://142.42.1.1/")
    assert URI.match("http://142.42.1.1:8080/")
    assert URI.match("http://➡.ws/䨹")
    assert URI.match("http://⌘.ws")
    assert URI.match("http://⌘.ws")
    assert URI.match("http://foo.com/blah_(wikipedia)#cite-1")
    assert URI.match("http://foo.com/blah_(wikipedia)_blah#cite-1")
    assert URI.match("http://foo.com/unicode_(✪)_in_parens")
    assert URI.match("http://foo.com/(something)?after=parens")
    assert URI.match("http://☺.damowmow.com/")
    assert URI.match("http://code.google.com/events/#&product=browser")
    assert URI.match("http://j.mp")
    assert URI.match("ftp://foo.bar/baz")
    assert URI.match("http://foo.bar/?q=Test%20URL-encoded%20stuff")
    assert URI.match("http://مثال.إختبار")
    assert URI.match("http://例子.测试")
    assert URI.match("http://उदाहरण.परीक्षा")
    assert URI.match("http://-.~_!$&'()*+,;=:%40:80%2f::::::@example.com")
    assert URI.match("http://1337.net")
    assert URI.match("http://a.b-c.de")
    assert URI.match("http://223.255.255.254")
    assert URI.match("https://foo_bar.example.com/")

