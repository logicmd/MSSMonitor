#!/usr/bin/env python
# -*- coding: utf-8 -*-

from string import Template

class UrlTemplate(Template):
    """docstring for SmoothStreamingUrlTemplate"""
    idpattern = r'[a-z][_a-z0-9]*(\.[a-z][_a-z0-9]*)*'



class SmoothStreamingMedia:
    def __init__(self):
        self.duration = -1
        self.video_quality = []
        self.audio_quality = []
        self.video_duration = []
        self.audio_duration = []
        self.base_url = ''
        self.video_url_template = ''
        self.audio_url_template = ''

    def build_url():
        if video_url_template and video_quality and video_duration:
            pass


if __name__ == '__main__':

    s = UrlTemplate('QualityLevels(${bitrate})/Fragments(audio=${start time})')
    maps = {'bitrate': '123', 'start time': '456'}
    print s.safe_substitute(maps)