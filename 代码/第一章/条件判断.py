#if语句语法规则：条件成立执行代码不成立不执行
money=500
if money>300:
    print(123)
print(456)
#条件成立执行代码1，不成立执行代码2
money=int(input("请输入你兜里的钱"))
if money>100:
    print ("火锅")
else:
    print("串串")

#if语句相互嵌套
money=int(input("请输入你兜里的钱"))
if money>1000:
    if money <= 5000:
        print("去北京")
    else:
      print("去国外")
else:
    print ("在家")
#第四种,esle和elif
money=int(input("请输入你兜里的钱"))
if money>1000:
    print("去北京")
elif money>500:
      print("海南")
elif money>100:
      print("aba")
else:
    print ("在家")
