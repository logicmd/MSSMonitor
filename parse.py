#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
from SmoothStreamingMedia import SmoothStreamingMedia
import json
from pprint import pprint
import Cookie

def config_writer():
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

def config_parser(files='conf/Request.json'):
    # Writing our configuration file to 'example.cfg'
    with open(files, 'r') as f:
        config=json.load(f)
        f.close()
        #print config
        #pprint(config)

        if config['Cookies']:
            Cookie_list = []
            for a_cookie in config['Cookies']:
                print a_cookie['Name'], a_cookie['Value']

                C = Cookie.BaseCookie()
                C[a_cookie['Name']] = a_cookie['Value']
                print C
                return
                if(a_cookie['Domain']):
                    C[a_cookie['Name']['domain']] = a_cookie['Domain']
                if(a_cookie['Path']):
                    C[a_cookie['Name']['path']] = a_cookie['Path']
                if(a_cookie['Expire']):
                    C[a_cookie['Name']['expire']] = a_cookie['Expire']
                if(a_cookie['Secure']):
                    C[a_cookie['Name']['secure']] = bool(a_cookie['Secure'])

                Cookie_list.append(C)

                print C
        return Cookie_list


def parse(manifest_content, manifest_url, SSM):
    # tree = ET.parse(manifest_file)
    # root = tree.getroot()
    root = ET.fromstring(manifest_content)
    if root.tag == 'SmoothStreamingMedia':
        SSM.duration = root.get('Duration')
        #print root.get('Duration')

    for stream_index in root:
        #print stream_index.tag, stream_index.attrib
        if stream_index.get('Type') == 'video':
            SSM.video_url_template = stream_index.get('Url')
            for stream_index_child in stream_index:
                if stream_index_child.tag == 'QualityLevel':
                    SSM.video_quality.append(stream_index_child.get('Bitrate'))
                if stream_index_child.tag == 'c':
                    SSM.video_duration.append(stream_index_child.get('d'))


        if stream_index.get('Type') == 'audio':
            SSM.audio_url_template = stream_index.get('Url')
            for stream_index_child in stream_index:
                if stream_index_child.tag == 'QualityLevel':
                    SSM.audio_quality.append(stream_index_child.get('Bitrate'))
                if stream_index_child.tag == 'c':
                    SSM.audio_duration.append(stream_index_child.get('d'))

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
    #config_writer()
    config_parser()