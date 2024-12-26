#1.字符串格式化问题
#我叫****，我住在****,我今年****,我喜欢做*****
# name=input("请输入你的名字")
# address=input("请输入你的地址")
# age=int("请输入你的年龄")
# hobby=input("请输入你的爱好")
# # %s 字符串占位    %d  占位整数    %f 占位小数
# s="我叫%s,我住在%s,我今年%d岁，我喜欢做%s" %(name,address,age,hobby)
# s0="我叫%s"%name
# s1= "我叫%s,我住在%s,我今年%d岁，我喜欢做%s".format(name,address,age,hobb)
# s2=f"我叫{name},我住在{adress},我今年{age}，我喜欢做{hobby}"#f-string推荐这个
# print(s)
# 2.索引和切片
#索引：按照位置提取元素
# s="我叫周杰伦"
# #采用索引方式提取某一个字符
# print(s[3])
# print(s[0])
# print(s[-1])#-表示倒数
#切片：从一个字符串中提取一部分内容
# s="我今天心情很好，你呢？你怎么样"
# print(s[3:6]) #从索引位置3进行切片，切到6结束，坑：切不到第二个位置元素
# 语法：s[start:end]从start切片取不到end
# print(s[:5]) #  如果start是从头开始切片，可以省略
# print(s[6:])  #  从6开始一直截取到末尾
# print(s[:])    #:两端有空白表示开头或结尾
# print(s[-3:-1])#  目前只能从左往右切
# s="123"
# # 给切片添加步长来控制切片方向
# print(s[::-1]) #-表示从右往左
# 语法：s[start:end:step] 从start到end，每step个元素出来一个元素
# s="12345678910"
# print(s[3:8:2])# 两个出来左边数字
# print (s[-1:-7:-2])# 倒着数。两边数字选右边
# 3. 字符串常规操作
# 字符串的操作一般不会对原字符串产生影响，一般是返回一个新的字符
# 3.1 字符串大小写转换
# s="python"
# s1=s.capitalize()  # 首字母大写
# print(s1)
# s="I have a dream!"
# s1=s.title()# 单词首字母大写
# print(s1)
# s="I HAVE A DREAM"
# s1=s.lower()# 变小写字母
# print(s1)
# s="i have a dream"
# s1=s.upper()# 变大写字母
# print(s1)
# 忽略大小写进行判断
# if verify_code.upper() == user_input.upper():
#     print("验证码正确")
# else:
#     print("验证码不正确")
# verify_code="xAd1"
# user_input=input(f"请输入正确的验证码（{verify_code}）:")
# 3.2 替换和切割
# strip()去掉字符串左右两端空白     s1=s.strip（）
# username=input("请输入用户名：")
# password=input("请输入密码：")
# if username=="admin":
#     if password=="123456":
#         print("登录成功")
#     else:
#         print ("登录失败")

# replace(old,new) 字符串替换,用什么切损失掉什么
# s="123"
# s1=s.replace("123","456")
# print(s1)
# split(用什么切割)字符串切割
# a="1!2!3"
# list=a.split("!")
# print(list)
#  3.4查找和判断
# 查找
# s="你好啊，我叫周润发"
# ret=s.find("周润发")#  返回值-1就是没有该字符串出现 ，换为index没有就报错
# print(ret)
# print()
# 判断
# name=input("请输入你的名字：")
# #判断你是不是姓张
# if name.startswith("张"):   #字符串是否以，，，开头，endswith（）
#     print("你姓张")
# else:
#     print("不姓张")

# money=input("请输入你兜里的钱")
#
# if money.isdigit():   #判断字符串是否由整数组成
#     money=int(money)
#     print("可以")
# else:
#     print("no")
#
#     #3.5补充和总结
#     s.split("用什么切割s")/////join连接
