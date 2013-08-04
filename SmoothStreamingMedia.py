#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import datetime
import os

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
        self.video_urls = []
        self.audio_urls = []

    def get_url_ism(self):
        if self.base_url:
            k = self.base_url.rfind('/')
            l = self.base_url.rfind('/', 0, k-1)
            return self.base_url[:k], self.base_url[l+1:k]

    def build_url(self):

        if self.video_url_template and self.video_quality \
            and self.video_duration:

            for vq in self.video_quality:
                cusum = 0
                for vd in self.video_duration:
                    self.video_urls.append(self.video_url_template\
                        .replace('{bitrate}', str(vq), 1)\
                        .replace('{start time}', str(cusum), 1))
                    cusum = cusum + int(vd)

        if self.audio_url_template and self.audio_quality \
            and self.audio_duration:

            for vq in self.audio_quality:
                cusum = 0
                for vd in self.audio_duration:
                    self.audio_urls.append(self.audio_url_template\
                        .replace('{bitrate}', str(vq), 1)\
                        .replace('{start time}', str(cusum), 1))
                    cusum = cusum + int(vd)


    def fetch_fragment(self, base_path='./Snapshot'):
        url_prefix, ism = self.get_url_ism()
        timestamp = str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
        if self.video_urls:
            path = base_path + '/' + timestamp + '/' + ism
            for vu in self.video_urls:
                i = vu.rfind('/')
                extended_path = vu[:i]

                file_path = path+'/'+extended_path
                file_name = vu[i+1:]
                url = url_prefix+'/'+vu

                if not os.path.exists(file_path):
                    os.makedirs(file_path)
                req = urllib2.Request(url)

                # Open the url
                try:
                    f = urllib2.urlopen(req)
                    print "downloading " + url

                    # Open our local file for writing
                    local_file = open(path+'/'+vu, "w")
                    #Write to our local file
                    local_file.write(f.read())
                    local_file.close()

                #handle errors
                except urllib2.HTTPError, e:
                    print "HTTP Error:",e.code , url
                except urllib2.URLError, e:
                    print "URL Error:",e.reason , url



if __name__ == '__main__':
    print datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # s = 'QualityLevels({bitrate})/Fragments(audio={start time})'
    # print  s.replace('{bitrate}', '200', 1).replace('{start time}', '300', 1)
