# uribuilder

> A library to help you build URI

[![Build Status](http://img.shields.io/travis/com/dexpota/uribuilder.svg?style=flat-square)](https://travis-ci.com/dexpota/uribuilder)
[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://dexpota.mit-license.org)


```
uri = scheme "://" (userinfo@)? host (:port)? (path-abempty / path-absolute / path-rootless / path-empty) [ "?" query ] [ "#" fragment ]
```