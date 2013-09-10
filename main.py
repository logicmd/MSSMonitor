#!/usr/bin/env python

# -*- coding: utf-8 -*-

import urllib2
import fetch as fetcher
import parse as parser
from SmoothStreamingMedia import SmoothStreamingMedia
import sys, getopt

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

def test_live():
    url = 'http://ss.logicmd.net/live/LiveSmoothStream.isml/Manifest'
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


def test_cookies_crawl():
    cookie_file = 'conf/Request.json'
    cookie_opener = parser.config_parse(cookie_file)

    manifest_dic = fetcher.fetch_manifest_from_file('./data/list.txt',cookie_opener)

    for (manifest_url,manifest) in manifest_dic.items():
        SSM = SmoothStreamingMedia()
        parser.parse(manifest, manifest_url, SSM)
        fetcher.fetch_fragment(SSM)


def usage():
    print 'main.py -u <UserAgent> -c <Cookies> OR'
    print '        --useragent <UserAgent> --cookies <Cookies>'

def main(argv):

    ua=''
    cookies=''
    url=''
    try:
        opts, args = getopt.getopt(argv,"ha:c:u:",["useragent=","cookies=","url="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit()
        elif opt in ("-a", "--useragent"):
            ua = arg
        elif opt in ("-c", "--cookies"):
            cookies = arg
        elif opt in ("-u", "--url"):
            url = arg


    #print 'ua ' + ua
    #print 'cookies ' + cookies
    #print 'url ' + url


    #main.py -a "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1581.2 Safari/537.36" -c "__utma=149734569.173931233.1374135637.1374156175.1374219909.3" -u "http://ss.logicmd.net/live/LiveSmoothStream.isml/Manifest"


    opener = parser.opener_builder(ua, cookies)

    SSM = SmoothStreamingMedia()
    SSM.opener=opener
    parser.parse(fetcher.fetch_manifest_with_cookies(url, opener), url, SSM)
    fetcher.fetch_fragment(SSM)


if __name__ == '__main__':
    #test_live()
    main(sys.argv[1:])
