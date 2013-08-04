#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2

def fetch_manifest(manifest_url):
    req = urllib2.Request(manifest_url)
    response = urllib2.urlopen(req)

    manifest = response.read() #.decode('utf-16')
    # If you want to print it properly added '.decode('utf-16')', or leave it alone
    return manifest


def fetch_manifest_from_file(file_name):
    f = open(file_name)
    manifest_dic = {}
    for line in f:
        manifest_dic[line] = fetch_manifest(line)
    return manifest_dic

def fetch_sample_manifest():
    return fetch_manifest('http://ss.logicmd.net/tears/tears_of_steel_720p.ism/Manifest')


def fetch_fragment(SSM):
    SSM.fetch_fragment()


if __name__ == '__main__':
    print fetch_sample_manifest()