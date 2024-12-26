#1.创建数组
#列表可以储存多种数据类型，数组只能有一种数据类型
#1.1根据python中列表生成
import numpy as np
a1=np.array([1,2,3.0])
print(a1)  #输出为[1.2.3]
print(type(a1))# <class 'numpy.ndarray'>
b1=np.array([4,5,"6"])
print(b1)   #有一个为字符串全为字符串--['4' '5' '6']

#1.2使用np.arange生成
a2=np.arange(10)
print(a2)  #[0 1 2 3 4 5 6 7 8 9]
b2=np.arange(0,10,2)
print(b2)    #[0 2 4 6 8]

#1.3使用np.random生成N行N列随机数组
a3=np.random.random((2,2))#2行2列数组
print(a3)
b3=np.random.randint(0,9,size=(4,4))
print(b3)# 元素从0-9之间随机的4行4列

# 1.4使用函数生成特殊数组
a4=np.zeros((2,2))  #生成元素都为0的2*2矩阵
a5=np.ones((3,3))    #生成元素都为1的3*3矩阵
a6=np.full((2,3),9)    #生成2*3矩阵，元素全为9
a7=np.eye(4)# 对称数组
#2.数组数据类型
b=np.array([1,2,3,4,5],dtype="i")  #指定dtype
print(b.dtype)     #int32
c=np.array([1,2,3,4,5],dtype=np.float16)
print(c.dtype)     # float16
c1=c.astype("i")    # 修改数据类型
print(c1.dtype)


