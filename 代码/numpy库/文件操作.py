# 操作csv文件
from array import array

import numpy as np
from partd.utils import frame

#np.savetxt(frame,array,fmt="文件写入格式",delimiter=None)#(文件、字符串、压缩文件，存入文件的数组，文件格式，分割字符串默认是任何空格)
scores=np.random.randint(0,100,size=(20,2))
np.savetxt("score.csv",scores,delimiter=",",header="英语，数学",fmt="%d")   #%d表示整型s
#读取文件
"""np.loadtxt(fram,dtype=np.float,delimiter=None,unpack=False)
    skiprows:跳过前面x行
    usecols：读取指定的列，用元组组合
    unpack：如果True，读取出来的数组是转置后的
"""
#np独有的存储解决方案
"""
存储： np.save(frame,array)或np.savez(frame,array),前者扩展名为.npy后者为.npz
加载：np.load(frame)
"""
c=np.random.randint(0,10,size=(2,3))
np.save("c",c)
b=np.loadtxt("score.csv",delimiter=",",skiprows=1)  #数组值不统一
print(b)
c1=np.load("c.npy")
print(c1)