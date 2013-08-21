#!/usr/bin/env python

# -*- coding: utf-8 -*-

import urllib2
import fetch as fetcher
import parse as parser
from SmoothStreamingMedia import SmoothStreamingMedia

def test1():
    url = 'http://vibox10.dev.fwmrm.net/hss_live.isml/Manifest'
    SSM = SmoothStreamingMedia()
    parser.parse(fetcher.fetch_manifest(url), url, SSM)
    for vu in SSM.video_urls:
        print vu

def test1f():
    url = 'http://vibox10.dev.fwmrm.net/hss_live.isml/Manifest'
    SSM = SmoothStreamingMedia()
    parser.parse(fetcher.fetch_manifest(url), url, SSM)
    fetcher.fetch_fragment(SSM)


def test2():
    path = './data/list.txt'
    manifest_dic = fetcher.fetch_manifest_from_file(path)
    for manifest_url in manifest_dic.keys():
        SSM = SmoothStreamingMedia()
        parser.parse(manifest_dic[manifest_url], manifest_url, SSM)
        fetcher.fetch_fragment(SSM)

def test3():
    url = 'http://ss.logicmd.net/tears/tears_of_steel_720p.ism/Manifest'
    cookie_file = 'conf/Request.json'
    cookie_opener = parser.config_parse(cookie_file)

    SSM = SmoothStreamingMedia()
    parser.parse(fetcher.fetch_manifest_with_cookies(url,cookie_opener), url, SSM)

    for vu in SSM.video_urls:
        print vu


def main():
    cookie_file = 'conf/Request.json'
    cookie_opener = parser.config_parse(cookie_file)

    manifest_dic = fetcher.fetch_manifest_from_file('./data/list.txt',cookie_opener)

    for (manifest_url,manifest) in manifest_dic.items():
        SSM = SmoothStreamingMedia()
        parser.parse(manifest, manifest_url, SSM)
        fetcher.fetch_fragment(SSM)

if __name__ == '__main__':
    test1f()
