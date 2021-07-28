import pandas as pd
import os
import predict
import collections
import json
import requests

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
    path = os.path.join(".","视频 "+name)
    PATH = '../data401-500'+path
    print(PATH)

    num0 = 0
    num1 = 1
    #data_str = open('../data401-500/视频 A-SOUL_Official/BV1Bv411L74f _ 《超级敏感》五一特别直播 纯享版.json',encoding="utf-8").read()
    for root,dirs,files in os.walk("../data401-500/视频 A-SOUL_Official"): 
        for file in files: 
            df = pd.read_json(os.path.join(root,file), orient = 'records')
            l = predict.main(df)
            d = collections.Counter(l)
            num0 += d[0] # number of negative
            num1 += d[1] # number of positive

    print(num1/(num1+num0))

main('703007996')