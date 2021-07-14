import requests
import json
import os
import time

from requests.api import head
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

def get_one_piece(rid,index):
    url = "https://api.live.bilibili.com/xlive/web-room/v1/dM/getDMMsgByPlayBackID?rid="+str(rid)+"&index="+str(index)
    res = requests.get(url,headers=headers)
    print("ok")
    danmaku_list=[]
    pieces_of_danmaku = json.loads(res.text)["data"]["dm"]["dm_info"]
    for one_piece_danmaku in pieces_of_danmaku:
        text = one_piece_danmaku["text"]
        uid = one_piece_danmaku["uid"]
        medal = one_piece_danmaku["medal"] #具体medal里面的内容，前面几个是最重要的，依次是牌子等级，牌子名称，主播名字，主播uid
        new_danmaku = {"text":text,"uid":uid,"medal":medal}
        danmaku_list.append(new_danmaku)

    # with open("test"+str(index)+".json","w",encoding="utf-8") as record_file:
    #     json_danmaku= json.dumps(danmaku_list,ensure_ascii=False)
    #     record_file.write(json_danmaku)
        
    return danmaku_list
    # with open("testagain.json","w",encoding="utf-8") as record_file:
        

    #     record_file.write(res.text)
    # one_piece_danmaku = json.loads(res.text)["data"]["dm"]["dm_info"][0]
    # print(one_piece_danmaku)
    # pass

def get_max_index(rid):
    url = "https://api.live.bilibili.com/xlive/web-room/v1/record/getInfoByLiveRecord?rid="+str(rid)
    res = requests.get(url, headers=headers)
    maxIndex = json.loads(res.text)["data"]["dm_info"]["num"]
    return maxIndex

def main(name,rid,title):
    index_limit = get_max_index(rid)
    all_danmaku=[]
    for index in range(0,index_limit):
        one_piece=get_one_piece(rid,index)
        all_danmaku.extend(one_piece)
        print(str(index)+" ok")
        # time.sleep(2)
    json_danmaku=json.dumps(all_danmaku,ensure_ascii=False)
    filename = os.path.join(".",name,rid+" && "+title+".json")
    
    try:
        with open(filename,"w",encoding="utf-8") as record_file:
            record_file.write(json_danmaku)
    except Exception as e:
        print(e)



if __name__ == "__main__":
    rid = input("请输入回放id\n")
    name="test"
    title="海边"
    main(name,rid,title)