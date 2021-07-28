import pickle
import os
import pandas as pd
import jieba


def chinese_word_cut(mytext):
    return " ".join(jieba.cut(mytext))


def main(df):
    with open('SAmodel.pkl', 'rb') as f:
        model = pickle.load(f)
    #df = pd.read_csv('test.csv', encoding='gb18030')
    test = df[['content']]

    test['cutted_comment'] = test.content.apply(chinese_word_cut)
    l = model.predict(test.cutted_comment)
    return l
#d = collections.Counter(l)
#print(d[0])


