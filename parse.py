#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
from SmoothStreamingMedia import SmoothStreamingMedia
import json
from pprint import pprint
import urllib2

def config_write():
    config = {}
    config['UserAgent'] =\
        'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1581.2 Safari/537.36'

    config['Cookies'] = []
    cookie = {}
    cookie['Name'] = '__utma'
    cookie['Value'] = '149734569.173931233.1374135637.1374156175.1374219909.3'
    cookie['Domain'] = ''
    cookie['Path'] = ''
    cookie['Expire'] = None
    cookie['Secure'] = None
    config['Cookies'].append(cookie)

    cookie = {}
    cookie['Name'] = '__utmz'
    cookie['Value'] = ' 149734569.1374135637.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'
    cookie['Domain'] = ''
    cookie['Path'] = ''
    cookie['Expire'] = None
    cookie['Secure'] = None
    config['Cookies'].append(cookie)



    # Writing our configuration file to 'example.cfg'
    with open('conf/Request.json', 'w') as f:
        f.write(json.dumps(config))
        f.close()

def config_parse(files='conf/Request.json'):
    # Writing our configuration file to 'example.cfg'
    with open(files, 'r') as f:
        config=json.load(f)
        f.close()
        #print config
        #pprint(config)


        opener = urllib2.build_opener()

        if config['UserAgent']:
            opener.addheaders.append(('User-agent', config['UserAgent']))


        if config['Cookies']:
            cookie_list=[]
            is_first=True
            for a_cookie in config['Cookies']:
                if not is_first:
                    cookie_list.append("; ")
                cookie_list.append(a_cookie['Name']+'='+a_cookie['Value'])

                if is_first:
                    is_first=False
            cookie_str=''.join(cookie_list)
            opener.addheaders.append(('User-agent', cookie_str))


    return opener


def parse(manifest_content, manifest_url, SSM):
    # tree = ET.parse(manifest_file)
    # root = tree.getroot()
    root = ET.fromstring(manifest_content)
    if root.tag == 'SmoothStreamingMedia':
        SSM.duration = root.get('Duration')
        SSM.is_live = root.get('IsLive')
        #print root.get('Duration')

    time_sync_point = 2

    for stream_index in root:
        #print stream_index.tag, stream_index.attrib
        if stream_index.get('Type') == 'video':
            SSM.video_url_template = stream_index.get('Url')
            for stream_index_child in stream_index:
                if stream_index_child.tag == 'c':
                    SSM.video_duration.append(int(stream_index_child.get('d')))
                    if time_sync_point>0:
                        #print stream_index_child.get('t')
                        if stream_index_child.get('t'):
                            SSM.video_ts_offset = int(stream_index_child.get('t'))
                            time_sync_point -= 1

                elif stream_index_child.tag == 'QualityLevel':
                    SSM.video_quality.append(stream_index_child.get('Bitrate'))





        if stream_index.get('Type') == 'audio':
            SSM.audio_url_template = stream_index.get('Url')
            for stream_index_child in stream_index:
                if stream_index_child.tag == 'c':
                    SSM.audio_duration.append(int(stream_index_child.get('d')))
                    if time_sync_point>0:
                        #print stream_index_child.get('t')
                        if stream_index_child.get('t'):
                            SSM.audio_ts_offset = int(stream_index_child.get('t'))
                            time_sync_point -= 1

                elif stream_index_child.tag == 'QualityLevel':
                    SSM.audio_quality.append(stream_index_child.get('Bitrate'))


    # For debug
    SSM.base_url = manifest_url
    SSM.build_url()


def open_file():
    f = open('data/Manifest_fetch.xml')
    return f.read()

if __name__ == '__main__':
    # SSM = SmoothStreamingMedia()
    # parse(open_file(), 'http://ss.logicmd.net/tears/tears_of_steel_720p.ism/Manifest', SSM)
    # for vu in SSM.video_urls:
    #     print vu
    config_parse()