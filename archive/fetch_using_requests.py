#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

def fetch_manifest(manifest_url):
    r = requests.get(manifest_url, stream=True)

    if r.status_code==200:
        print r.raw.read(10)


def fetch_sample_manifest():
    fetch_manifest('http://ss.logicmd.net/tears/tears_of_steel_720p.ism/Manifest')

if __name__ == '__main__':
    fetch_sample_manifest()