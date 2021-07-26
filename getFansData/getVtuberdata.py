my_url = 'https://api.live.bilibili.com/xlive/general-interface/v1/rank/getHeartRank?ruid=%s&;amp;page=%s&page_size=100'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
import json
import requests
import pymysql
vtuber_data = []
vtuber_id = []
vtuber_name = []
with open('D:/vtuber/1.json','r',encoding='utf8')as fp:
    json_data = json.load(fp)
    for k in range(1,500):
        name = ""
        for i in range(30):
            if(json_data[k][i]=='e'):
                for j in range(i,30):
                    if (json_data[k][j + 4] == '\"'):
                        break;
                    name = name + json_data[k][j+4]
        vtuber_name.append(name)
vtuber_name.append("赫卡Tia")
with open('D:/vtuber/1.json','r',encoding='utf8')as fp:
    json_data = json.load(fp)
    for j in range (1,500):
        sum = ""
        for i in range(2,20):
            if(json_data[j][i].isdigit()):
                sum = sum + json_data[j][i]
            else:
                break
        vtuber_id.append(sum)
vtuber_id.append(693)
for i in range(500):
    d = {"vtuber_id": vtuber_id[i],
        "vtuber_name":vtuber_name[i]}
    if (i % 10 == 0):
        print("*********************************************************************")
    print(d)
    vtuber_data.append(d)
print(vtuber_data)
data=[]
for k in range(500):
    response = requests.get(my_url%(vtuber_id[k],1),headers=headers)
    json_data = json.loads(response.text)
    num = json_data["data"]["num"]
    my_json = json_data["data"]["item"]
    for i in range(1,100):
        response = requests.get(my_url%(vtuber_id[k],i),headers=headers)
        json_data = json.loads(response.text)
        my_json = json_data["data"]["item"]
        if(len(my_json)==0):
            break
        for j in range(0,len(my_json)):
            l = {"user_id":my_json[j]["uid"],
                "user_name":my_json[j]["name"],
                "target_id":my_json[j]["target_id"],
                "medal_name":my_json[j]["medal_name"]}
            print(l)
            data.append(l)


conn = pymysql.connect(host='localhost',
                       user='root',
                       password='233033',
                       db='vtuber',
                       charset='utf8')
cursor = conn.cursor()
sql = " REPLACE INTO `vtuber`.`fans`(`user_id`, `target_id`, `user_name`, `medal_name`) VALUES (%s, %s, %s, %s)"
i = 0
for my in data:
    cursor.execute(sql, [my["user_id"],my["target_id"], my["user_name"], my["medal_name"]])
    i+= 1
    print(i)
print('------------------------------------------')
conn.commit()   # 提交，不然无法保存插入或者修改的数据(这个一定不要忘记加上)
print('???????????????????????????????????????????????????')
cursor.close()  # 关闭游标
print('++++++++++++++++++++++++++++++++++++++++++++')
conn.close()  # 关闭连接
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='233033',
                       db='vtuber',
                       charset='utf8')
cursor = conn.cursor()
sql = " REPLACE INTO `vtuber`.`vtuber`(`vtuber_id`, `vtuber_name`) VALUES (%s, %s)"
i = 0
for my in vtuber_data:
    cursor.execute(sql, [my["vtuber_id"],my["vtuber_name"]])
    i+= 1
    print(i)
print('------------------------------------------')
conn.commit()   # 提交，不然无法保存插入或者修改的数据(这个一定不要忘记加上)
print('???????????????????????????????????????????????????')
cursor.close()  # 关闭游标
print('++++++++++++++++++++++++++++++++++++++++++++')
conn.close()  # 关闭连接