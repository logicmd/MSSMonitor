MSSMonitor
==========
A python-based MSS Monitor which runs a preflight check on the Ad candidate to be inserted. It checks a group parameter within the ad and the video to improve the ad playback quality and avoid ad insertion failure.


Usage
-----
Use main.py to initiate the crawler

    main.py -u <UserAgent> -c <Cookies> OR
            --useragent <UserAgent> --cookies <Cookies>'

Performance
-----------
最初部分是满速爬取，之后为412后休眠降速所致。

![performance](https://github.com/logicmd/MSSMonitor/blob/master/%E5%90%9E%E5%90%90%E6%80%A7%E8%83%BD.png?raw=true)

需求
----

  1. [o]直播，解析tfrf
  2. [o]多线程按时间顺序开始的时候并行下载多个quality level
  3. [o]接受命令行参数 curl 参数
  4. [o]live (fragmentinfo=)
  5. [o]http code 412 (还没压好)，延时1s或者fragment的时间 - opener error code handler
  6. [o]live存Manifest，Live加时间戳文件名
  7. live检验 video 和 audio的timestamp相差是否太大（定时刷新（10s）从Manifest取Cue Point，打log说这个qpoint插是否有问题）
  8. fps-去找每个fragment里面帧数
  9. 打log输出汇总信息，是否成功/失败下载了Fragment；输出音视频时间戳误差的信息
  10. 多线程的同时下载相同时间戳的Fragment
  11. 7*24 rotate log etc


关于合作
--------

HLS数据比HSS多，HLS有master list和media list（分别代表不同的quality），可以看到media list进出，但是看不到取了多少个ts chunk。

关于buffering，除非在客户端取。

关于输出的需求

  1. 能够介入Moternization report
  2. 对于广告有统计意义的结论。 广告看视频高清的比例
  3. 能够对设定quality level有意义。低的码率、高的码率取消，过密的码率取消
  4. 从UserAgent角度找平台限制
  5. 从IP角度找ISP和带宽限制


