import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
df=pd.DataFrame(np.random.randn(5,4))
df1=np.abs(df) #取绝对值
# #通过apply将函数应用到列或者行
# f=lambda x:x.max()    #匿名函数
# print(df1.apply(f))
#通过applymap将函数应用到每个数据
f2=lambda x:'%.2f'%x   #保留两位小数
a=df.applymap(f2)
print(a)