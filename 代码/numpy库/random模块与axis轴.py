import numpy as np
np.random.seed(1)   #种子设置好数值不再变
np.random.rand()
np.random.rand()#0-1之间随机数
np.random.rand(2,3,4)# 2块3行四列的数组，数组值0-1
np.random.randn(2,3) #生成2行3列数组，数组中数值满足正态分布
np.random.randint(0,10,size=(3,4))  #生成值在0-10之间，3行4列的数组
data=np.arange(5)
np.random.choice(data,size=(2,3)) #从data中随机选样，生成2行3列数组
np.random.choice(data,3) #从data中随机采样3个数据形成一维数组
np.random.choice(10,3) #从0-10之间随机取3个值
a=np.arange(8)
np.random.shuffle(a)#将a元素位置进行随即变换



# axis相关
x=np.array([[1,2],[3,4]])
x.sum(axis=0)  #[4,5]  最外面
x.max(axis=1) #拿到每个元素的直接子元素在求最大值
np.delete(x,o,axis=1) #找到最外面括号下的直接子元素的第0个，然后删掉最后剩一行元素/按照axis=1删除会把第一列数据删掉