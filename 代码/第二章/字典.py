#  字典， 以键值形式进行存储数据
#  字典表示方式;{key:value,key2:value}
# dic = {"jay": "周杰伦", "金毛狮王": "谢逊"}
# val = dic["jay"]  #把索引换成了key
# print(val)
#字典的key必须可哈希的数据类型
#字典的value可以是任何数据类型

    #字典的增删改查
#
# dic = dict()
# dic["jay"]="周杰伦"

# dic[1] = 123
# print(dic)
# dic[1] = 234   # 字典里面已经有key1，此时执行修改操作
# print(dic)
# dic.setdefault("tom","胡辣汤")#设置默认值，如果以前有tom，setfault失效
# print(dic)
#
#   #删除  -根据key删除
# # dic.pop("jay")
# # print(dic)
#
# #查询
# print(dic["jay"])  # key不存在，程序报错，确定key没问题可以用
# print(dic.get("jay"))   # key不存在，程序返回None，  不确定key用


#None--单纯就是空，表示没有

# 字典的循环和嵌套
# dic={"赵四":"A",
#      "刘三":"B",
#      "王大":"C"
# }
# 用for循环直接拿到key
# for key in dic:
#      print(key,dic[key])
#
#
# #把所有的key全保存在一个列表
# print(list(dic.keys()))
#
# #把所有value放一个列表
# print(list(dic.values()))



# print(list(dic.items()))
# for key,value in dic.items():   #可以直接拿到字典中的key和dic
#    print(key,value)
#

# a,b=(1,2)   #元组或列表都可以执行该操作，该操作被称为解构（解包）
# print(a)
# print(b)

#字典的嵌套
# wangfeng = {
#      "name":"汪峰",
#      "age":18,
#      "wife":{
#           "name":"章子怡",
#           "hobby":"演习",
#           "assistant":{
#                "name":"樵夫",
#                "age":19,
#                "hobby":"打游戏"
#
#           }
#      },
#      "children":[
#           {"name":"孩子1","age":13},
#           {"name":"孩子2","age":11},
#           {"name":"孩子3","age":10},
#      ]
# }
# #汪峰妻子助手的名字
# name=wangfeng['wife']['assistant']['name']
# print(name)
#
# #汪峰的第二个孩子加1岁
# wangfeng['children'][1]['age']=wangfeng['children'][1]['age']+1
# print(wangfeng)

#字典的循环删除
dic={"赵四":"A",
     "刘三":"B",
     "王大":"C"
}
temp=[]  #存放即将要删除的key
for key in dic :
     if key.startswith("王"):
          temp.append(key)
for t in temp: #循环列表删除字典中内容
     dic.pop(t)
     print(dic)
