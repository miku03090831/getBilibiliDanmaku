## B站视频弹幕爬取

#### 功能简介

通过视频的BV号来爬取这个视频的所有弹幕，同时会记录下弹幕发送者的uid

B站对视频的弹幕发送者uid做了加密处理，也就是说不让你查到是谁发的弹幕

这一点通过decrypt.py来实现破解

破解的代码完全来自下面的地址，感谢大佬

https://github.com/Aruelius/crc32-crack

#### 使用方法

安装好所有的依赖库，最笨的方法就是告诉你缺啥你就pip install啥

`python getDanmakuByBvid.py` 使用时请确保python和py文件的路径正确

程序会记录下每一条弹幕的发送者uid和内容

最终爬取到的结果会存到同目录下，与视频同名的json文件当中