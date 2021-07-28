import pandas as pd
import os
import predict
import collections
import json
import requests
import math
import re

'''
for file in flie_dir:
    if not os.path.isdir(file):
      
        flie_name = path  + file
        print(flie_name)
        data = io.imread(flie_name)

for root,dirs,files in os.walk("../data401-500/视频 A-SOUL_Official/"):
    data_str = os.path.join(root,files)
    df = pd.read_json(data_str,orient = 'records')
    arr = bycsv.main(df)
'''
def main(uid):
    url = "https://api.bilibili.com/x/space/acc/info?mid="+uid+"&jsonp=jsonp"
    res = requests.get(url)
    res.encoding="utf-8"
    print(res)
    name = json.loads(res.text)["data"]["name"]
    path = "视频 "+name
    # PATH = '../data401-500'+path
    root_path = os.path.join(".","danmaku")
    print(root_path)
    print(path)
    dir_name = "bad"
    for root,dirs,files in os.walk(root_path):
        for dir in dirs:
            if re.findall(path,dir):
                dir_name = os.path.join(root_path,dir)
    PATH = dir_name
    # print(PATH)
    if PATH=="bad":
        return -1

    num0 = 0
    num1 = 1
    #data_str = open('../data401-500/视频 A-SOUL_Official/BV1Bv411L74f _ 《超级敏感》五一特别直播 纯享版.json',encoding="utf-8").read()
    for root,dirs,files in os.walk(PATH): 
        for file in files: 
            # print(os.path.join(root,file))
            try:
                df = pd.read_json(os.path.join(root,file), orient = 'records',encoding="utf-8")
                l = predict.main(df)
                d = collections.Counter(l)
                num0 += d[0] # number of negative
                num1 += d[1] # number of positive
            except Exception as e:
                pass


    return (num1/(num1+num0))

def analysis_all():
    uid_list=[]
    with open("NameList.txt","r",encoding="utf-8") as name_file:
        names = name_file.readlines()
        for n in names:
            uid = n.strip().split(",")[0]
            uid_list.append(uid)

    with open("positiveRate.txt","a+",encoding="utf-8") as posi_rate:
        for uid in uid_list:
            result = main(uid)
            if result==-1:
                continue
            rate = math.ceil(result*10000)/100
            print("%s完毕"%(uid))
            print(rate)
            posi_rate.write("%s,%f\n"%(uid,rate))


# main('1926156228')
analysis_all()