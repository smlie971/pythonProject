# 用户输入一个数字判断是不是35的倍数
import numpy

n=int(input("来个数:"))
if n%35==0:
    print("是35的倍数")
else:
    print("不是35的倍数")
#矩阵运算
import numpy
x=numpy.ones(3)#ones（）用于生成全1的矩阵
m=numpy.eye(3)*3#eye（）用于生成单位矩阵
m[0,2]=5#设置指定位置上元素的值
x@m#矩阵相乘
"""
1.算数运算
+ - *  /(除)%（余）//(整)
2.比较运算
>< >= <= == !=
3.赋值运算
  = += -= *=
  a+=b
  a=a+b
4.逻辑运算
and
or
not

5.成员运算
"""
