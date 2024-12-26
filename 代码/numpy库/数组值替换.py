import numpy as np
a=np.random.randint(0,10,size=(3,5))
print(a)
a[1]=np.array([1,2,3,4,5])   #替换第一行
print(a)
a[a<3]=1   #<3的元素替换为1
#使用where替换
result=np.where(a<5,0,1)  #<5替换为1，>5替换为0

