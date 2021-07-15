import requests
import json
import ByBvid
import os

def get_video_list(uid):
    pass

def get_page_video(uid,page,name):
    url = "https://api.bilibili.com/x/space/arc/search?mid="+uid+"&ps=30&tid=0&pn="+str(page)+"&keyword=&order=pubdate&jsonp=jsonp"
    res = requests.get(url,headers=headers)
    res.encoding="utf-8"
    v_list = json.loads(res.text)["data"]["list"]["vlist"]
    for video in v_list:
        bvid = video["bvid"]
        ByBvid.main(bvid,name)


def main(uid):
    # 首先获取up主名字，创建相应文件夹
    url = "https://api.bilibili.com/x/space/acc/info?mid="+uid+"&jsonp=jsonp"
    res = requests.get(url,headers=headers)
    res.encoding="utf-8"
    name = json.loads(res.text)["data"]["name"]
    path = os.path.join(".","视频 "+name)
    isExist = os.path.exists(path)
    if not isExist:
        os.makedirs(path)

    #然后获取up主的投稿视频列表，先知道一共有多少页投稿（每页30个视频）
    url="https://api.bilibili.com/x/space/arc/search?mid="+uid+"&ps=30&tid=0&pn=1&keyword=&order=pubdate&jsonp=jsonp"
    res = requests.get(url,headers=headers)
    res.encoding="utf-8"
    info = json.loads(res.text)["data"]
    total_nums = info["page"]["count"]
    page_nums = total_nums//30+1
    # page_limit = 5 if page_nums > 5 else page_nums # 最多爬取5页的视频（150个）
    page_limit = 1 if page_nums > 1 else page_nums # 先爬取一页试试
    for page in range(1,page_limit+1):
        get_page_video(uid,page,name)  # 逐页爬取

if __name__ == "__main__":
    uid = input()
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
    main(uid)

    