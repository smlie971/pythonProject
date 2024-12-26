#一列索引2列数据
#Dataframe构建-----2类方法
#1.字典类
import  numpy as np
import pandas as pd
#数组、列表、元组构成的字典构造Dataframe
#构造一个字典
data={'a':[1,2,3,4],
      'b':(5,6,7,8),
      'c':np.arange(9,13)}
#构造Dataframe
frame=pd.DataFrame(data)
print(frame)
#index属性查看索行引
frame.index     #0-3
#columns属性查看列索引
frame.columns   # abc
#values查看值
frame.values
#指定Index
frame=pd.DataFrame(data,index=['A','B','C','D'])
#指定行索引
frame=pd.DataFrame(data,index=['A','B','C','D'],columns=['a','b','c','d'])
#2.Series构成的字典构造Dataframes
pd1=pd.DataFrame({'a':pd.Series(np.arange(3)),
                  'b':pd.Series(np.arange(3,5))})
#3.字典构成的字典构造Dataframe
#字典嵌套
data1={
    'a':{'apple':3.6,'banana':5.6},
    'b':{'apple':3,'banana':5},
    'c':{'apple':3.2}
}
pd2=pd.DataFrame(data1)
print(pd2)
#ndarray 构造Dataframe
arr1=np.arange(12).reshape(4,3)
frame1=pd.DataFrame(arr1)
print(arr1)
#字典构成的列表构造Dataframe
l1=[{'apple':3.6,'banana':5.6},{'apple':3,'banana':5}, {'apple':3.2}]
pd3=pd.DataFrame(l1)
print(pd3)
#series构成的列表构造Dataframe
l2=[pd.Series(np.random.rand(4)),pd.Series(np.random.rand(2))]   #2行4列
pd4=pd.DataFrame(l2)
print(pd4)
pd5=pd.DataFrame(np.arange(9).reshape(3,3),index=['a','b','c'],columns=['A','B','C'])
#和numpy 一样转置
pd5.T
pd['D']=9 #数据增加一列索引为D元素为9
del(pd['d']) #删除该列

