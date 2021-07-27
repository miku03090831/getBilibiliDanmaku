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

# 关于如何修改星系图相关：

## 边相关

1. 边太多了（太少了） 

   修改后端Server.py中getEdges()函数中limit变量的值，是相关度的下限（取值在0.15往上有点少，在0.1往下有点多）

2. 边的粗细

   后端Server.py中搜索`lineStyle`,里面的width。目前设置的粗细是100倍的（相关度-相关度下限）

3. 边的颜色

   同2，修改color

4. 边的长短

   在前端中src/views/Home.vue中修改graphInit()函数中的option变量，下面的force属性中的edgeLength属性（边长的上下限，具体长度和相关度有关，越相关越短），也与force中的repulsion（斥力）和gravity（向中心的引力）有关，比较玄学

   

## 点相关

1. 点的大小

   后端Server.py中getNodes()的symbolSize

2. 点的颜色

   同上，在itemStyle中设置color





