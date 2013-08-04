#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
from SmoothStreamingMedia import SmoothStreamingMedia




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
    SSM = SmoothStreamingMedia()
    parse(open_file(), 'http://ss.logicmd.net/tears/tears_of_steel_720p.ism/Manifest', SSM)
    for vu in SSM.video_urls:
        print vu