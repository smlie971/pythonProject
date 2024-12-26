#数据的存储与读取
import numpy as np
import pandas as pd

# df=pd.read_csv('工作表.csv')  #要放在同一目录下.默认分隔符，
# print(df)
# df0=pd.read_table('工作表.csv',sep=',')  #默认分隔符为制表,加sep
# print(df0)
# df1=pd.read_csv('工作表.csv',header=None)   #使用默认列名
# print(df1)
# df2=pd.read_csv('工作表.csv',names=['a','b','message'])#自定义列名
# print(df2)
# df3=pd.read_csv('工作表.csv',names=['a','b','message'],index_col='message')#指定列索引变为行索引
# print(df3)
df4=pd.read_csv('ex1.csv')
print(df4)
pa=df4=pd.read_csv('ex1.csv',index_col=['key1','key2'])    #key1,key2前后顺序不一样运行结果不一样
print(pa)
df4.to_csv('out_ex1.csv')   #写入，输出一个文件




#将json转换为python
import json
res=json.loads()#将json转换为python
#将python转换为json
res1=json.dumps()
sib=pd.DataFrame(res1[''],columns=[])#取res一部分


#分块读取大文件
agg1=pd.read_csv(r'文件路径',chunksize=10)#读取10行
agg1.head(10)#读取前10行
print(agg1.get_chunk(10))#获取agg1 读取10行




