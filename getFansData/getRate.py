import json
import pymysql
vtuber_data = []
vtuber_id = []
vtuber_name = []
list = []
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
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='233033',
                       db='vtuber',
                       charset='utf8')
cursor = conn.cursor()
sql = "SELECT count(*) FROM vtuber.fans " \
      "WHERE target_id=%s and user_id in " \
      "(SELECT user_id from vtuber.fans GROUP BY user_id HAVING COUNT(user_id)>=2)"
sql1 =  "SELECT count(*) FROM vtuber.fans " \
      "WHERE target_id=%s"
for i in range(500):
    try:
       # 执行SQL语句
       cursor.execute(sql,vtuber_id[i])
       # 获取所有记录列表
       results = cursor.fetchall()
       for row in results:
           a = row[0]
    except:
       print ("Error: unable to fetch data")
    try:
       # 执行SQL语句
       cursor.execute(sql1,vtuber_id[i])
       # 获取所有记录列表
       results = cursor.fetchall()
       for row in results:
           b = row[0]
    except:
       print ("Error: unable to fetch data")
    list.append(1-a/b)
    print(1-a/b)
for i in range(500):
    l = {"rate": list[i],
         "vtuber_id": vtuber_id[i]}
    print(l)
    vtuber_data.append(l)
conn.close
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='233033',
                       db='vtuber',
                       charset='utf8')
cursor = conn.cursor()
sql = " REPLACE INTO `vtuber`.`rate`(`rate`,`vtuber_id`) VALUES (%s,%s)"
i = 0
for i in range(500):
    cursor.execute(sql, [vtuber_data[i]["rate"],vtuber_data[i]["vtuber_id"]])
print('------------------------------------------')
conn.commit()   # 提交，不然无法保存插入或者修改的数据(这个一定不要忘记加上)
print('???????????????????????????????????????????????????')
cursor.close()  # 关闭游标
print('++++++++++++++++++++++++++++++++++++++++++++')
conn.close()  # 关闭连接