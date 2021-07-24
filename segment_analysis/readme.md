# 情感分析

使用 train.py 训练出 SAmodel.pkl 模型，再用 predict.py 进行预测。
主程序为 predictbyuid.py 

输入uid，输出正面弹幕的比例

文件要求：segment_analysis文件与'data401-500/XX/XX.json'的data401-500文件夹为同一层级
使用总数据库时，将 predictbyuid.py 中的'data401-500'改为数据库所在文件夹即可