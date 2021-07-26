from flask import Flask,request,abort,jsonify
import os
import re
import math
import random

import json
app=Flask(__name__)


@app.route("/api/hotword",methods=['POST'])
def hot_word(): #获取词云图
    # print(request.body)
    uid = request.json["uid"]
    # print(uid)
    with open("NameList.txt","r",encoding="utf-8") as name_file:
        names = name_file.readlines()
        for name in names:
            if name.strip().split(",")[0] == uid:
                uidname = name.strip().split(",")[1]
    
    pathname = os.path.join(".","wordCountResult")
    regex = uidname
    for root,dirs,files in os.walk(pathname):
        for file in files:
            if re.findall(regex,file):
                filename = os.path.join(pathname,file)

    word_dict={}
    with open(filename,"r",encoding="utf-8") as hot_word_file:
        word_dict={}
        words = hot_word_file.readlines()[1:]
        for word in words:
            hot = word.strip().split(",")[0]
            freq = word.strip().split(",")[1]
            word_dict[hot]=freq
    return jsonify(word_dict)



@app.route("/api/getinfo",methods=['POST'])
def get_info():  #获取uid，粉丝数，单推人比例，等等信息（详见fansInfo.json)
    uid = request.json["uid"]
    with open("fansInfo.json","r",encoding="utf-8") as fans:
        info = json.load(fans)
        
    return jsonify(info[uid])

@app.route("/api/getNodes",methods=["POST"])
def getNodes():  # 获取力引导图的节点
    nodes = []
    with open("fansInfo.json","r",encoding="utf-8") as fans:
        info = json.load(fans)
        for uid in info:
            name=info[uid]["name"]
            fans_num=info[uid]["fans_num"]# 仅用作在des中展示
            des="the number of fans is "+str(fans_num)# 悬停在节点上时显示的提示语，显示粉丝数量
            size = math.sqrt(fans_num)*2.5
            uid_info = {
                "uid":uid,
                "name":name,
                "fans_num":fans_num,
                "des":des,
                "symbolSize":size,
                "itemStyle":{
                    "color":random.choice(["#FF9966","#CCCCFF","#99CCCC","#99CCFF","#FFFFCC","#FFFF99"])
                }
            }
            nodes.append(uid_info)
    return jsonify(nodes)

@app.route("/api/getEdges",methods=["POST"])
def getEdge(): # 获取力引导图的边
    edges = []
    uid_list=[]
    with open("relevance.json","r") as rele_file:
        rele = json.load(rele_file)
    with open("fansInfo.json","r",encoding="utf-8") as fans:
        info = json.load(fans)
        for uid in info:
            uid_list.append(uid)
    # 对于list中的每一个uid，去构造以它为起点，其他节点为终点的边

    for uid in uid_list:
        target = rele[uid] # 一个dict，记录了uid这个节点，和其他所有节点的相关度
        for item in target:
            if item not in uid_list:#不是up主（混进来的测试节点。。。）
                continue
            if item == uid: #自己到自己的边不画
                continue
            if item < uid: # 两个点只能画出来一条边，不知道为啥。画两遍也是一条边，干脆只画一条边
                continue
            if target[item] >= 0.15: 
                e = {
                    "source":info[uid]["name"],
                    "target":info[item]["name"],
                    "curveness":0.9,
                    "name":math.ceil(target[item]*100)/100,
                    "value":target[item],
                    "lineStyle":{
                        "color":random.choice(["#993366","#336699","#FF6600","#663300","#6699FF"]),
                        "width":1.5
                    }
                }
                edges.append(e)

    return jsonify(edges)



if __name__ == "__main__":
    app.run(debug=True,threaded=False)