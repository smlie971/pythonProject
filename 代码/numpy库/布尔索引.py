import numpy as np
a2=np.arange(24).reshape(4,6)
(a2<10)    #小于10元素为Ture，大于为False
a2[a2<10]  #把小于10的元素提出来
a2[(a2<5)|(a2>10)]   #提取a2<5或a2>10的元素
#布尔索引：通过相同数组上的True还是False进行提取，提取条件有多个，用&代表且，用|代表或，如果有多个，每个条件要用圆括号括起来

