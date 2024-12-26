#计算机表示小数有误差
#bool用来做条件判断，取值范围：True，False
#基础数据类型之间的转换
# a="10"#字符串
# print(type(a))
# b=int(a)#把字符串转化成int
# print(type(b))
# a=10    #python中非零的数字都为True，零是False
# b=bool(a)
# print(type(b))
# print(b)
# while 1:  #死循环，恒为真
#      print("haha")
s=""#在python中，所有的非空字符串都是True,空字符串都是False
print(bool(s))
#在python中表示空的东西都为False，不空的东西都为False
while 1:
    content=input("请输入你要喷的内容：")
    if content:
        print ("输入内容",content)
        break
        