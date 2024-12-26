#  不拷贝
import numpy as np
a=np.arange(12)
b=a    #  这种情况不会进行拷贝
print(b is a)    #返回True说明a和b相同

#浅拷贝
a=np.arange(12)
c=a.view()
print(c is b)    #返回False说明不同
c[0]=100
print(a[0])  #打印100 ，说明对c上改变会影响a上面的值，说明指向空间一样
#深拷贝
d=a.copy()
d[0]=100
print(a[0])      #打印0，说明d和a指向的内存空间完全不同了


