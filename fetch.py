#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2


def parse(manifest_content):
    for atype in manifest_content.findall('SmoothStreamingMedia'):
        print(atype.get('Duration'))


def fetch_manifest(manifest_url):
    req = urllib2.Request(manifest_url)
    response = urllib2.urlopen(req)


    manifest = response.read()
    return manifest


def fetch_sample_manifest():
    fetch_manifest('http://ss.logicmd.net/tears/tears_of_steel_720p.ism/Manifest')



if __name__ == '__main__':
    parse(fetch_sample_manifest())