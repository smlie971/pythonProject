import numpy as np
# 1.一维数组的索引和切片
a1=np.arange(10)
print(a1)    #[0 1 2 3 4 5 6 7 8 9]
#  1.1进行索引操作
print(a1[4])    #4
#   1.2进行切片操作
print(a1[4:6])    #[4,5]
#  1.3使用步长
print(a1[::2])     #[0 2 4 6 8]
#   1.4使用负数作为索引(倒着来)
print(a1[-1])  #9
# 2.多维数组  (也是使用中括号来索引切片，使用逗号进行分割，前为列，后为行，只有一个值就是行)
a2=np.random.randint(0,10,size=(4,6))
print(a2)
print(a2[0])   #第一行
print(a2[1:3])  #第一行、第二行---连续索引
print(a2[0,2,3])  #第0、2、3行
print(a2[1,1])  #前行后列取具体元素
print(a2[1,2],[4,5])  #第一行第四列和第四行第五列的两个元素
print(a2[1:3,4:6])   # 取第一行第二行，第四列第五列元素 ---连续索引
print(a2[:,1]) #第一列
print(a2[:,[1,3]])  # 取第一列和第三列