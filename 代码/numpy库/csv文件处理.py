#从csv中读取数据
import csv
with open('score.csv','r') as fp:
    reader=csv.reader(fp)
    next(reader)
    for x in reader:   #reader迭代器
        #获取具体数据用索引
        print(x)
def read_csv_demo2():
    with open('score.csv','r') as fp:
        #使用DictReader创建的reader对象
        #不会包含标题那行数据
        #reader是一个迭代器，遍历迭代器返回字典
        reader=csv.DictReader(fp)
        for x in reader:
            #通过key读取
            print(x)
if __name__ == '__main__':
    read_csv_demo2()



#写入数据到csv
headers={'username','age','height'}  #表头信息
values={
    ('张三',18,180),
    ('李四',18,170),
    ('王五','16',160)
}
with open('classroom.csv','w',encoding='utf-8',newline='') as fp:
    writer=csv.writer(fp)
    writer=csv.writer(fp)
    writer.writerrow(headers)
    writer.writerow(values)
def writer_csv_demo2():
    headers={'username','age','height'}
    values={
        {'username':'张三','age':10,'height':180},
        {'username':'李四','age':11,'height':179}
    }
    with open('classroom.csv', 'w', encoding='utf-8', newline='') as fp:
        writer=csv.DictWriter(fp,headers)   #字典形式写入
        #写入表头信息需要调入writeheader方法
        writer.writeheader()
        writer.writerws(values)
if __name__ == '__main__':
    writer_csv_demo2()