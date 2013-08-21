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
        self.urls = []
        self.is_live = None
        self.video_ts_offset = ''
        self.audio_ts_offset = ''

    #def info(self):
    #    s='VDuration is ' + self.duration + '/n'
    #    + ''

    def get_url_ism(self):
        if self.base_url:
            k = self.base_url.rfind('/')
            l = self.base_url.rfind('/', 0, k-1)
            return self.base_url[:k], self.base_url[l+1:k]

    def build_url(self):

        v_flag = self.video_url_template and self.video_quality and self.video_duration
        a_flag = self.audio_url_template and self.audio_quality and self.audio_duration

        if v_flag or a_flag:

            if self.video_ts_offset:
                v_cusum = int(self.video_ts_offset)
            else:
                v_cusum = 0

            if self.audio_ts_offset:
                a_cusum = int(self.audio_ts_offset)
            else:
                a_cusum = 0


            if not len(self.audio_duration) == 0:
                a_avg = float(sum(self.audio_duration))/len(self.audio_duration)
                #计算音频frag的平均时长，因为音频frag长度比较稳定
                #时间戳相差超过半个音频frag后尝试暂停audio或者video下载

                v_fnum=len(self.video_duration)
                a_fnum=len(self.audio_duration)
                i=0
                j=0
                v_replacable = False
                a_replacable = False
                if 'Fragments' in self.video_url_template:
                    v_replacable = True
                if 'Fragments' in self.audio_url_template:
                    a_replacable = True

                while i<v_fnum or j<a_fnum:

                    minus = v_cusum - a_cusum

                    if minus < a_avg/2 and i<v_fnum:

                        for vq in self.video_quality:
                            frag_url=self.video_url_template\
                                .replace('{bitrate}', str(vq), 1)\
                                .replace('{start time}', str(v_cusum), 1)

                            self.urls.append(frag_url)
                            if v_replacable:
                                self.urls.append(frag_url.replace('Fragments','FragmentInfo'))

                        v_cusum = v_cusum + self.video_duration[i]
                        i+=1


                    if minus > -a_avg/2 and j<a_fnum:
                        for aq in self.audio_quality:
                            frag_url = self.audio_url_template\
                                .replace('{bitrate}', str(aq), 1)\
                                .replace('{start time}', str(a_cusum), 1)

                            self.urls.append(frag_url)
                            if a_replacable:
                                self.urls.append(frag_url.replace('Fragments','FragmentInfo'))

                        a_cusum = a_cusum + self.audio_duration[j]
                        j+=1


    def sub_fetch_manifest(self, url_prefix, path):

        #Fetch Manifest

        timestamp = str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))

        file_path = path
        file_name = timestamp+'.manifest'
        url = url_prefix +'/Manifest'

        if not os.path.exists(file_path):
            os.makedirs(file_path)
        req = urllib2.Request(url)

        # Open the url
        try:
            f = urllib2.urlopen(req)
            print "downloading manifest--"+url

            # Open our local file for writing
            local_file = open(file_path+'/'+file_name, "w")
            #Write to our local file
            local_file.write(f.read())
            local_file.close()

        #handle errors
        except urllib2.HTTPError, e:
            print "HTTP Error:",e.code , url
        except urllib2.URLError, e:
            print "URL Error:",e.reason , url


    def fetch_fragment(self, base_path='./Snapshot'):
        url_prefix, ism = self.get_url_ism()
        timestamp = str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))

        path = base_path + '/' + timestamp + '/' + ism

        self.sub_fetch_manifest(url_prefix, path)

        #Fetch Fragment
        counter = 1
        if self.urls:

            for u in self.urls:
                i = u.rfind('/')
                extended_path = u[:i]

                file_path = path+'/'+extended_path
                file_name = u[i+1:]
                url = url_prefix+'/'+u

                if not os.path.exists(file_path):
                    os.makedirs(file_path)
                req = urllib2.Request(url)

                # Open the url
                try:
                    f = urllib2.urlopen(req)
                    print "[%d]downloading %s" %(counter, url)
                    counter += 1

                    # Open our local file for writing
                    local_file = open(path+'/'+u, "w")
                    #Write to our local file
                    local_file.write(f.read())
                    local_file.close()

                #handle errors
                except urllib2.HTTPError, e:
                    print "HTTP Error:",e.code , url
                except urllib2.URLError, e:
                    print "URL Error:",e.reason , url

    def get_traf(self,fs='D:/Develop/Python/MSSMonitor/Snapshot/2013-08-21_16-13-21/hss_live.isml/QualityLevels(160000)/Fragments(audio=5210980193189)'):
        chunk = 1048576 * 4
        uuid = '\x00\x00\x00\x2c\x75\x75\x69\x64'
        if isinstance(fs, basestring):
            f = open(fs,'rb')
        else:
            f = fs
        eof = False

        s = ''
        while uuid not in s:
            s = f.read(chunk)
            if not s:
                eof = True
                break
            uuid_loc = s.find(uuid)

            traf = int(s[uuid_loc+30:uuid_loc+36],16)
            print traf

if __name__ == '__main__':
    #print datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    SSM = SmoothStreamingMedia()
    SSM.get_traf()
    # s = 'QualityLevels({bitrate})/Fragments(audio={start time})'
    # print  s.replace('{bitrate}', '200', 1).replace('{start time}', '300', 1)
