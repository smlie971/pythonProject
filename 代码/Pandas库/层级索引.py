import numpy as np
import pandas as pd
s1=pd.Series(np.random.randn(12),index=[['a','a','a','b','b','b','c','c','c','d','d','d'],[0,1,2,0,1,2,0,1,2,0,1,2]])
print(s1)
#选取
#外层选取
print(s1['b'])
#内层获取
print(s1[:,0])
#交换内外层索引
print(s1.swaplevel())
#先对外层索引进行排序，然后对内层索引进行排序，默认升序
print(s1.sortlevel())
