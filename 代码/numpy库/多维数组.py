import numpy as np
# np.ndim #数组维度
a1=np.array([1,2,3])
print(a1.ndim)   #1表示数组维度1
a2=np.array([[1,2,3],[4,5,6]])
print(a2.ndim)

# ndarray.shape    数组维度的元组
print(a1.shape)   #(3,),一个元素说明是一维
print(a2.shape)    #(2, 3),两个元素说明二维

# ndarray.reshape    修改数组维数
a3=a2.reshape((1,6))
print(a3)   #[[1 2 3 4 5 6]]
print(a3.ndim)   #2
a4=a2.reshape((6,))
print(a4)   #[1 2 3 4 5 6]
print(a4.ndim)   #1

#ndarray.size  总元素的个数
count=a4.size
print(count)

#ndarray.itemsize   数组每个元素占内存的大小，单位字节
itemise=a3.itemsize
print(itemise)
print(a3.dtype)
print(itemise*a3.size)   # itemise*size=总数组大小