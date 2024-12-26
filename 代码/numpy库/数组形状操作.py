import numpy as np
"""reshape 不会修改原数组形状，只会返回修改后结果，resize 会直接修改"""
a1=np.random.randint(0,10,size=(3,4))
a1.reshape((2,6))    #不修改数组本身
a1.resize((4,3))

"""flatten将数组转换为1维数组，将拷贝返回回去,后续对返回值进行修改不影响之前的数组
   ravel将数组转换为1维数组后，在将视图引用回去，后续对返回值修改影响之前的数组
"""
# 数组组合操作

vstack1=np.random.randint(0,10,size=(3,4))
print(vstack1)
vstack2=np.random.randint(0,10,size=(2,4))
print(vstack2)
vstack3=np.vstack((vstack1,vstack2)) #垂直方向叠加一起，列必须一致
print(vstack3)
h1=np.random.randint(0,10,size=(3,4))
h2=np.random.randint(0,10,size=(3,1))
h3=np.hstack((h1,h2))     #平行方向叠加一起，行必须一致
print(h3)
"""
concatenate可以手动指定axis参数具体那个方向叠加，如果axis=0，代表在水平方向叠加，如果axis=1，代表在垂直方向叠加，如果axis=None，先进行叠加在转换成1维数组
"""
#   数组的切割
#1.split：用于指定分割成几列。
hs1=np.random.randint(0,10,size=(3,4))
print(hs1)
b1=np.hsplit(hs1,2)  #切为两部分
b2=np.hsplit(hs1,(1,2))  #在第1行后切一刀，，在2后切一刀行
#2.vsplit：分割成几行
vs1=np.random.randint(0,10,size=(4,5))
np.vsplit(vs1,4)   # 平均分成4部分
np.vsplit(vs1,(1,3))
np.hsplit(hs1,4,axis=1)   #axis=0意思按行切割，axis=1，意思按列切割


#  数组转置
a2=a1.T  # a1转置
#transpose   返回值为View，修改返回值，会影响到原来数组。、