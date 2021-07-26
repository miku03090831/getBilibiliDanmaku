# 关于 爬取弹幕
爬取b站视频弹幕（包括弹幕内容，发送者uid）
爬取b站直播回放弹幕（包括弹幕内容，发送者uid，佩戴的粉丝牌子）

# 关于最终展示

frontend里面是前端，采用vue搭建

backend里面是后端，采用flask搭建

## backend

运行方式：有python环境即可，根据自己情况，缺什么就pip install什么

运行命令`python Server.py`

## frontend

运行方式：首先安装nodejs环境（百度nodejs官网下载），

安装完nodejs后，先全局安装vue-cli，命令是`npm install -g @vue/cli`

速度慢就改用cnpm（具体方法百度）或者挂梯子

然后在frontend文件夹下，打开终端，输入`npm install`即可自动安装全部依赖

然后`npm run serve`运行，成功后在浏览器地址栏输入`localhost:8080`即可访问前端界面（需要先把后端运行起来）





