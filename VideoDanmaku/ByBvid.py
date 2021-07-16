import requests
import json
from bs4 import BeautifulSoup
import decrypt
import os

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

def get_danmaku(bv,name):
    url = "http://api.bilibili.com/x/web-interface/view?bvid="+str(bv)
    res = requests.get(url, headers=headers)
    res.encoding='utf-8'
    try:
        staff = json.loads(res.text)["data"]["staff"]
        return 
    except:
        pass

    title = get_title(bv)
    cid  = get_cid(bv)
    url = "https://api.bilibili.com/x/v1/dm/list.so?oid="+str(cid)
    res = requests.get(url, headers=headers)
    res.encoding='utf-8'
    xml_text = res.text
    soup = BeautifulSoup(xml_text,"lxml")
    danmaku_list = []
    d_list = soup.find_all("d")
    decrypt.create_table()
    for i in d_list:
        content = i.string
        p_attrs = i.get('p').split(",")
        encrypted_uid = p_attrs[6]
        decrypted_uid = decrypt.main(encrypted_uid)
        d_obj = {'uid':decrypted_uid,'content':content}
        danmaku_list.append(d_obj)
        print("爬取"+str(len(danmaku_list))+"条")
        
    
    # with open("danmaku_xml.xml","w",encoding='utf-8') as xml_file:
    #     xml_file.write(xml_text)
    filename = os.path.join(".","视频 "+name,bv+" && "+title+".json")
    try:
        with open(filename,"w",encoding='utf-8') as json_file:
            json_danmaku = json.dumps(danmaku_list,ensure_ascii=False)
            json_file.write(json_danmaku)
    except:
        pass
            
def get_title(bv):
    url = "http://api.bilibili.com/x/web-interface/view?bvid="+str(bv)
    res = requests.get(url, headers=headers)
    info = json.loads(res.text)['data']
    title = info["title"]
    print(title)
    return title


def get_cid(bv):
    url = "https://api.bilibili.com/x/player/pagelist?bvid="+bv+"&jsonp=jsonp"
    res = requests.get(url, headers=headers)
    info = json.loads(res.text)['data']
    cid = info[0]['cid']
    return cid

def main(bv,name):
    get_danmaku(bv,name)

if __name__ == "__main__":
    bv=input()
    name = "七海Nana7mi"
    main(bv,name)