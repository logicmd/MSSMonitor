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
