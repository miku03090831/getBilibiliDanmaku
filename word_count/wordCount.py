import numpy as np
import pandas as pd
import jieba
import jieba.analyse
import codecs
import os

# 以小狼XF为例统计其所有视频里弹幕的词频
path = '../VideoDanmaku/视频 小狼XF'
path_list=os.listdir(path)

# 读取停用词表
stopwords = [line.strip() for line in codecs.open('stopped.txt', 'r', 'utf-8').readlines()]

segments = {}
for dir in path_list:
    df = pd.read_json(path+'/'+dir)
    for index, row in df.iterrows():
        content = row[1]
        #TextRank 关键词抽取，只获取固定词性
        words = jieba.cut(content)
        for word in words:
            # 停用词判断，如果当前的关键词不在停用词库中才进行记录
            if word not in stopwords:
                # 记录全局分词
                if word not in segments:
                    segments[word]=1
                else:
                    segments[word] = segments[word]+1
word_counts = pd.DataFrame(list(segments.items()),columns=['word','count'])
word_counts.set_index(['word'],inplace=True)
word_counts.to_csv('demo.csv')