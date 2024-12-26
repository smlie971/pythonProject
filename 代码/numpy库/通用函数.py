"""
一元函数
np.abs :绝对值
np.sqrt: 开根
np.square :平方
np.exp :计算指数
np.log ,np.log10: 以e为底，以10为底
np.sign :将数组中值标签化，大于0的变成1，等于0的变成0，小于0的变成-1
np.ceil :朝正无穷大方向取整，5.1变为6，-6.3变为-6
np.floor: 朝负无穷大方向取整，比如5.1变为5，-6.3变为-7
np.rint/np.round :返回四舍五入后的值
np.modf :将整数和小数分割开来形成两个数组
np.isnan : 判单是否是nan
np.isinf : 判断是否inf
np.cos/np.cosh/np.sin、np.arccos....  :三角函数
二元函数：
np.add(a,b) :加法运算
np.subtract :减法运算
np.negative: 负数运算
np.multiply : 乘法运算
np.divide: 除法运算
np.floor_divide : 整除运算
np.mod :取余运算
greater，greater_equal,less,less_equal,equal,not_equal: >,>=,<,<=,=,!=
logical_and: &
logical_or: |
聚合函数
np.sum :计算元素的和
np.prod: 计算元素的积
np.mean :计算元素的平均值
np.std :计算元素大的标准差
np.var : 计算元素方差
np.min/max: 计算元素最小值/最大值
np.argmin/argmax : 找出最小值的索引/最大值的索引
np.median: 元素的中位数
布尔数组函数
np.any  :验证一个元素是否为真
np.all ：验证所有函数是否为真
排序
np.sort(a): 指定轴进行排序，默认最后一个轴进行排序
np.sort(a,axis=0) 按照列排序
np.argsort:返回下标值
-np.sort(-a) 降序

其他函数
np.apply_along_axis: 沿着某个轴执行指定的函数
np.apply_along_axis(lambda x:x[(x!=x.max()&(x!=x.min())].mean(),axis=1,arr=a
#求数组啊按行求平均值，主要去掉最大值和最小值
np.linspace()用来将指定区间内的值平均分成多少分
np.linspace(0,1,12)# 将0-1分成12份生成一个数组
np.unique  :返回数组中的唯一值
np.unique(a,reurn_counts=True) #返回数组a唯一值并且返回每一个唯一值出现的次数

"""

import numpy as np
a=np.random.uniform(-10,10,size=(3,5)) #uniform平均分布
