import requests
import json
import getDanmakuOfRecord
import os
import logging
import time

from requests.api import get

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

def get_info(uid):
    url = "https://api.bilibili.com/x/space/acc/info?mid="+str(uid)+"&jsonp=jsonp"
    res = requests.get(url,headers=headers)
    res.encoding="utf-8"
    res_dict = json.loads(res.text)["data"]
    name = res_dict["name"]
    room_id = res_dict["live_room"]["roomid"]
    return name,room_id

def get_list_pagenums(roomid):
    url="https://api.live.bilibili.com/xlive/web-room/v1/record/getList?room_id="+str(roomid)+"&page=1&page_size=20"
    res = requests.get(url,headers=headers)
    res.encoding="utf-8"
    text = json.loads(res.text)
    count = text["data"]["count"]
    pagenums = count//20 + 1
    return pagenums

def get_records_by_roomid(name,roomid):
    pagenums = get_list_pagenums(roomid)
    for i in range(0,pagenums):
        pagenum = i+1
        url = "https://api.live.bilibili.com/xlive/web-room/v1/record/getList?room_id="+str(roomid)+"&page="+str(pagenum)+"&page_size=20"
        res = requests.get(url,headers=headers)
        res.encoding="utf-8"
        text = json.loads(res.text)
        record_list = text["data"]["list"]
        for index in range(0,len(record_list)):
            rid = record_list[index]["rid"]
            title = record_list[index]["title"]
            try:
                getDanmakuOfRecord.main(name,rid,title)
                print(str(rid)+"爬取完毕,休息2秒")
                time.sleep(2)
            except:
                logging.error("page "+str(pagenum)+" video "+str(index+1)+" error,perhaps no danmaku. rid:"+str(rid))
                

def main():
    uid = input("请输入主播uid:\n")
    (name,roomid)=get_info(uid)
    path = os.path.join(".",name)
    isExist = os.path.exists(path)
    if not isExist:
        os.makedirs(path)
    print("alive")
    get_records_by_roomid(name,roomid)
    # print(name)
    # print(roomid)


if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR,  
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',  
                    datefmt='%a, %d %b %Y %H:%M:%S',  
                    filename='./error_log.txt',  
                    filemode='a+')  
    main()
