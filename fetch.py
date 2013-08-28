#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import parse as parser

def fetch_manifest(manifest_url):
    req = urllib2.Request(manifest_url)
    response = urllib2.urlopen(req)

    manifest = response.read() #.decode('utf-16')
    # If you want to print it properly added '.decode('utf-16')', or leave it alone
    return manifest

def fetch_manifest_with_cookies(manifest_url,opener):
    f = opener.open(manifest_url)

    manifest = f.read() #.decode('utf-16')
    # If you want to print it properly added '.decode('utf-16')', or leave it alone
    return manifest


def fetch_manifest_from_file(file_name,opener=None):
    f = open(file_name)
    manifest_dic = {}
    if not opener:
        for line in f:
            manifest_dic[line] = fetch_manifest(line)
    else:
        for line in f:
            manifest_dic[line] = fetch_manifest_with_cookies(line,opener)

    return manifest_dic

def fetch_sample_manifest():
    return fetch_manifest('http://ss.logicmd.net/tears/tears_of_steel_720p.ism/Manifest')

def fetch_sample_manifest_with_cookies(opener):
    return fetch_manifest_with_cookies('http://ss.logicmd.net/tears/tears_of_steel_720p.ism/Manifest',opener)


def fetch_fragment(SSM):
    if SSM.is_live:
        SSM.fetch_live_fragment()
    else:
        SSM.fetch_fragment()


if __name__ == '__main__':
    opener=parser.config_parse()
    print fetch_sample_manifest_with_cookies(opener)