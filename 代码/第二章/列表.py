# 在python中用[]表示列表,元素用，隔开
#特性
# 有索引和切片
# list=["1","2","3","4","5"]
# print(list[2])
# print(list[1:3])#取不到3位置元素
# print(list[::-1])
# print(list[::-2])
# for item in list:
#     print(list)
# print(len(list))

# 列表增删改查
# lst=[]
#
# lst.append("a")#向列表中添加内容append（）追加
# lst.append("b")
# lst.append("c")
#
# lst.insert(0,"d")# insert（）插入
#
# lst.extend(["1","2","3"])#extend()合并两个列表，批量添加
# ret=lst.pop(3)#给出被删除的索引，返回被删除的元素
# print(lst)
# print(ret)
# lst.remove("a")#删除某个元素
# print(lst)

#修改
# lst[0]="haha"#直接用索引进行查询操作
# print(lst)
#
# #查询
# print(lst[0])

#把所有姓张的人修改成姓王
# lst=["赵敏","张绍刚","张三","伍德","张大","小乔"]
# for i in range(len(lst)):#可以直接拿到列表索引的for循环
#     item=lst[i]#item是列表中每一项
#     if item.startswith("张"):
#         new_name="王"+item[1:]
#         print(new_name)
#         lst[i]=new_name
# print(lst)

#列表排序
# lst=[1278990,123,1234,12345,123456]
# lst.sort()#对列表进行升序
# print(lst)
# lst.sort(reverse=True)
# print(lst)


#列表嵌套
lst=["abc","def",["123","1a1",["A","Bb"]],"ABC","DEF"]
print(lst[2][2][1])
lst[2][2][1]=lst[2][2][1].upper()
print(lst)

#列表循环删除
lst=["赵敏","张绍刚","张三","伍德","张大","小乔"]
temp=[]
for item in lst:
    if item.startswith("张"):
        temp.append(item)#把要删除的内容记下来
for item in temp:
    lst.remove(item)#去原列表中进行删除操作
    print(lst)

#安全稳妥的删除方式：将要删除的内容保存在新列表中，循环新列表，删除老列表
