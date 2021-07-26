import numpy as np
import pandas as pd
import jieba
import jieba.analyse
import codecs
import os

def save_word(path,path_list,name):
    segments = {}
    filename = os.path.join(".","wordCountResult",name+".csv")
    print("%s准备"%(filename))
    for dir in path_list:
        df = pd.read_json(path+'/'+dir,encoding="utf-8")
        for index, row in df.iterrows():
            content = row[1]
            #TextRank 关键词抽取，只获取固定词性
            words = jieba.cut(content)

            try:
                for word in words:
                # 停用词判断，如果当前的关键词不在停用词库中才进行记录
                    if word not in stopwords:
                        # 记录全局分词
                        if word not in segments:
                            segments[word]=1
                        else:
                            segments[word] = segments[word]+1
            except Exception as e:
                pass
    segments = list(segments.items())
    segments.sort(key=lambda x:x[1],reverse=True)
    segments = segments[:50]
    word_counts = pd.DataFrame(segments,columns=['word','count'])
    word_counts.set_index(['word'],inplace=True)
    word_counts.to_csv(filename)
    

# 以小狼XF为例统计其所有视频里弹幕的词频
# path = '../VideoDanmaku/视频 小狼XF'
stopwords = [line.strip() for line in codecs.open('stopped.txt', 'r', 'utf-8').readlines()]
# root_path="./danmaku"
root_path = os.path.join(".","danmaku")
for root,dirs,files in os.walk(root_path):
    for d in dirs:
        pathname = os.path.join(root,d)
        name = d[3:]
        path_list=os.listdir(pathname)
        save_word(pathname,path_list,name)


# 读取停用词表
stopwords = [line.strip() for line in codecs.open('stopped.txt', 'r', 'utf-8').readlines()]

