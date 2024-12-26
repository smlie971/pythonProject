#索引排序
import numpy as np
import pandas as pd
#
# s1=pd.Series(np.arange(4),index=list('dbca'))
# print(s1)
# print(s1.sort_index())   #默认升序
# s1.sort_index(ascending=False)   #降序
pd1=pd.DataFrame(np.arange(12).reshape(4,3),index=list('bdca'),columns=list('BCA'))
# #按照行排序
# pd1.sort_index()
# pd1.sort_index(axis=1)   #按照列排序
#
#
# #按值排序
# print(s1.sort_values())      #按值排序，有缺失值默认排最后
# print(s1.sort_values(ascending=False))
# print(pd1.sort_values(by=['A','B']))
pd2=pd.DataFrame({'a':[3,7,8,0],'b':[1,-1,4,8],'c':[0,6,-3,2]})
print(pd2)
print(pd2.sort_values(by='b'))  #按照指定一列
print(pd2.sort_values(by=['a','c'],ascending=False))     #按照指定多列进行排序

#唯一值和成员属性
s1=pd.Series([2,6,8,9,8,3,6],index=['a','a','c','c','c','c','c'])
s2=s1.unique()  #返回一个数组
print()
print(s1.value_counts()) #统计出现个数
s1.isin([8]) #判断值是否存在返回的布尔类型
s1.isin([8,2])  #判断多个值
data=pd.DataFrame({'a':[3,7,0,9],'b':[1,-1,4,8],'c':[0,6,-3,-2]})
print(data.isin([2,4]))



#处理缺失数据
df3=pd.DataFrame([np.random.randn(3),[1,2,np.nan],[np.nan,4,np.nan],[1,2.,3.]])
print(df3.isnull())
#丢弃缺失值dropna（）
print(df3.dropna())   #默认丢弃行
print(df3.dropna(axis=1))  #丢弃列
#填充缺失值
print(df3.fillna(-100))
