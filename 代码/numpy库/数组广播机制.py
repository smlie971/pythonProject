#  数组与数的计算
import numpy as np
a1=np.random.randint(0,5,size=(3,5))
a1*2   #每个数都变为2倍
a2=np.random.randint(0,5,size=(3,5))
a1+a2  #对应位置的值相加
a3=np.random.randint(0,5,size=(3,4))
a4=np.random.randint(0,5,size=(3,1))
a1+a4   # 行相同，加到每一列上，
a5=np.random.randint(0,5,size=(1,5))
a1+a5  # 列相同，加到每一行上面


"""
广播原则：
shape为（3，8，2）的数组不能和（8，3）数组进行运算，因为2和3不相等
shape为（3，8，2）可以和（8，1）运算，按照广播原则从后往前，2和1虽然不相等但是有一方长度为1，所以可以运算
"""

