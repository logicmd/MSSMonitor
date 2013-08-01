#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
from SmoothStreamingMedia import SmoothStreamingMedia




def parse(manifest_content, SSM):
    tree = ET.parse(manifest_content)
    root = tree.getroot()
    if root.tag == 'SmoothStreamingMedia':
        SSM.duration = root.get('Duration')
        #print root.get('Duration')

    for stream_index in root:
        #print stream_index.tag, stream_index.attrib
        if stream_index.get('Type') == 'video':
            for stream_index_child in stream_index:
                if stream_index_child.tag == 'QualityLevel':
                    SSM.video_quality.append(stream_index_child.get('Bitrate'))
                if stream_index_child.tag == 'c':
                    SSM.video_duration.append(stream_index_child.get('d'))

        if stream_index.get('Type') == 'audio':
            for stream_index_child in stream_index:
                if stream_index_child.tag == 'QualityLevel':
                    SSM.audio_quality.append(stream_index_child.get('Bitrate'))
                if stream_index_child.tag == 'c':
                    SSM.audio_duration.append(stream_index_child.get('d'))


def open_file():
    f = open('data/Manifest.xml')
    return f.read()

if __name__ == '__main__':
    SSM = SmoothStreamingMedia()
    parse('data/Manifest.xml', SSM)