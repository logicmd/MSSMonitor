MSSMonitor
==========


Useage
------
Use main.py to initiate the crawler


需求
----
    1.直播，解析tfrf
[o] 2.多线程按时间顺序开始的时候并行下载多个quality level
    3.接受命令行参数 curl 参数
[o] 4.live (fragmentinfo=)
    5.http code 412 (还没压好)，延时1s或者fragment的时间 - opener error code handler
    6.（live）检验 video 和 audio的timestamp相差是否太大（定时刷新（10s）从Manifest取QPoint，打log说这个qpoint插是否有问题）
    7.（live）存Manifest，Live加时间戳文件名
    8.fps-去找每个fragment里面帧数
