#series创建一列标签一列数据
#1.通过列表创建
import pandas as pd
s1=pd.Series([1,2,3,4,5])     #输出结果左边为索引，右边为值
#2.通过数组创建
import numpy as np
arr1=np.arange(1,6)   #[1,2,3,4,5]
s2=pd.Series(arr1)
s2=pd.Series(arr1,index=['a','b','c','d','e'])   #索引由12345修改为abcde#索引长度和数据长度必须相同
s1.values  #打印数值
s1.index   #打印索引
#3.通过字典创建
dict={'name':'李宁','age':'18','class':'三班','sex':''}
s3=pd.Series(dict,index=['name','age','class'])



#Series基本用法
s3.isnull()  #判断是否为空，空就是True
s3.notnull()   #判断是否不为空，非空True

#通过索引获取数据
print(s3.index)
print(s3.values)
#下标
s3[0]    #李宁
#标签
s3['age']    #18
#选取多个
s3[[1,3]]    #s3[['name’，‘age’]]  #name 李宁/age 18/
#切片
s3[1:3]  #age 18/class  三班-------下标切片取不到右端
#标签切片
s3['name':'class']     #能取到右端
#布尔索引
s2[s2>3]  #d 4/e 5
#索引用于数据对应关系不被运算结果影响
#name属性
s2.name='temp'   #对象名
s2.index.name='year'    #对象索引名
s2.head() #默认前5行
s2.tail() #默认后5行


