import numpy as np
import pandas as pd
ps1=pd.Series(range(5),index=['a','b','c','d','e'])
print(ps1)
pd1=pd.DataFrame(np.arange(9).reshape(3,3),index=['a','b','c'],columns=['A','B','C'])
# #索引对象不可变保证了数据安全性
print(pd1)
#索引的一些基本操作
#增

#reindex创建一个符合新索引的新对象
ps2=ps1.reindex(['a','b','c','d','e','f'])
print(ps2)
#行索引重建
pd2=pd1.reindex(['a','b','c','d'])
print(pd2)
#列索引重建
pd3=pd1.reindex(columns=['C','B','A'])
print(pd3)

#删
del ps1['b']
print(ps1)
#drop删除轴上的数据
#删除一条
ps4=ps1.drop('e')   #会产生新的对象
print(ps4)
#删除多条
ps5=ps1.drop(['c','d'])
print(ps5)
#删除列
pd2=pd1.drop('A',axis="columns")
print(pd2)
#inplace属性   在原对象上删除，并不会返回新的对象

#改
pd2.loc['b','B']=1000
print(pd2)   #修改（b,B）元素为1000



#高级索引
#1.loc标签索引---基于标签名的索引
print(ps1)
print(ps1[['a','c']])
print(ps1.loc[['a','c']])
print(pd1)
print(pd1.loc['a':'c','A'])   #第一个参数索引行，第二个参数索引列
#2.iloc位置索引
print(ps1.iloc[1:3])
print(pd1.iloc[0:2,0]) #前两行第一列


from sklearn.linear_model import LogisticRegression

