#!/usr/bin/env python

# -*- coding: utf-8 -*-

import urllib2
import fetch as fetcher
import parse as parser
from SmoothStreamingMedia import SmoothStreamingMedia

def test1():
    url = 'http://ss.logicmd.net/tears/tears_of_steel_720p.ism/Manifest'
    SSM = SmoothStreamingMedia()
    parser.parse(fetcher.fetch_manifest(url), url, SSM)
    for vu in SSM.video_urls:
        print vu

def test2():
    path = './data/list.txt'
    manifest_dic = fetcher.fetch_manifest_from_file(path)
    for manifest_url in manifest_dic.keys():
        SSM = SmoothStreamingMedia()
        parser.parse(manifest_dic[manifest_url], manifest_url, SSM)
        fetcher.fetch_fragment(SSM)


def main():
    manifest_list = []
    fetcher.fetch_manifest_from_file('D:/Develop/Python/MSSMonitor/data/list.txt', manifest_list)
    for manifest in manifest_list:
        SSM = SmoothStreamingMedia()
        parser.parse(manifest, SSM)
        fetcher.fetch_fragment(SSM)

if __name__ == '__main__':
    test2()
