#!/usr/bin/env python
# -*- coding: utf-8 -*-




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

    def build_url(self):
        if self.video_url_template and self.video_quality \
            and self.video_duration:

            for vq in self.video_quality:
                cusum = 0
                for vd in self.video_duration:
                    self.video_urls.append(self.base_url+self.video_url_template\
                        .replace('{bitrate}', str(vq), 1)\
                        .replace('{start time}', str(cusum), 1))
                    cusum = cusum + int(vd)

        if self.audio_url_template and self.audio_quality \
            and self.audio_duration:

            for vq in self.audio_quality:
                cusum = 0
                for vd in self.audio_duration:
                    self.audio_urls.append(self.base_url+self.audio_url_template\
                        .replace('{bitrate}', str(vq), 1)\
                        .replace('{start time}', str(cusum), 1))
                    cusum = cusum + int(vd)


if __name__ == '__main__':
    s = 'QualityLevels({bitrate})/Fragments(audio={start time})'
    print  s.replace('{bitrate}', '200', 1).replace('{start time}', '300', 1)
