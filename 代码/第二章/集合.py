# set集合,set集合无序，
# s={1,2,3}
# print(type(s))
#
# # python中的set集合进行数据存储的时候，需要对数据进行哈希计算，根据计算出来的哈希值进行储存
# #set集合要求存储的数据必须是可以进行哈希计算
# #不可哈希：  可变的数据类型：list，dict，set
# #可哈希：不可变的数据类型，int，str，tuple，bool，
# s=set()    #创建空集合
# s.add("123")
# s.pop()#由于集合无序，测试的时候无法验证是最后一个
# s.remove("123")
#想修改，先删除在新增


#交集，并集，差集
# s1={"a","b","c","d","e","f"}
# s2={"b","h","k","l"}
# print(s1&s2) #交集
# print(s1.intersection(s2))
#
# print(s1|s2)  #并集
# print(s1.union(s2))
#
# print(s1-s2)   #差集
# print(s1.difference(s2))

#重要的作用，可以去除重复

lst=["1", "1", "2", "3", "4", "5", "6"]
print(set(lst))
print(list(set(lst)))# 去除重复之后的数据无序

