import numpy as np
import pandas as pd
#Series
s1=pd.Series(np.arange(4),index=['a','b','c','d'])
s2=pd.Series(np.arange(5),index=['a','c','e','f','g'])
print(s1+s2)   #相同部分执行相加
#DataFrame
df1=pd.DataFrame(np.arange(12).reshape(4,3),index=['a','b','c','d'],columns=list('ABC'))
df2=pd.DataFrame(np.arange(9).reshape(3,3),index=['a','d','f'],columns=list('ABD'))
print(df1)
print(df2)
print(df1+df2)
#Dataframe与Series混合运算---广播Series的索引匹配DataFrame列索引



