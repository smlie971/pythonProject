s="周杰伦"
bs1=s.encode("gbk")
bs2=s.encode("utf-8")
print(bs1)
print(bs2)


#   把gbk字节转化为utf-8的字节
bs=b'\xd6\xdc\xbd\xdc\xc2\xd7'   # 先变字符串
s=bs.decode("gbk")     #解码
bs2=s.encode("utf-8")    #重新编码
print(bs2)
    #1.str.encode("编码")    进行编码
    #2.bytes.decode("编码")   进行解码
s="你好"
print(s.encode("gbk"))

