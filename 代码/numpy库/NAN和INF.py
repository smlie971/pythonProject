import numpy as np
data=np.random.randint(0,10,size=(3,5))
data=data.astype(np.float64)
data[0,1]=np.NAN
print(data)
#删除缺失值
data[1,2]=np.NAN
print(data[~np.isnan(data)])  #删除所有NAN值
lines=np.where(np.isnan(data))[0]    #获取所有包含nan的行
print(np.delete(data,lines,axis=0))     #只有delete0删除行，1删除列
#用其他值替代空值
scores=np.loadtxt("score.csv",delimiter=',',skiprows=1,dtype=np.str_)
scores[scores=='']=np.NAN#非数字字符串先转换为NAN
scores1=scores.astype(np.float64)
scores1[np.isnan(scores1)]=0  #求总分NAN用0代替
scores1.sum(axis=1)  #sun----1表示行，0表示列
scores2=scores1.copy
scores2=scores.astype(np.float64)
for x in scores2.shape[1]:  #取第2行
    col=scores2[:,x]   #取列
    non_nan_col=col[~np.isnan(col)]  #均值替换nan
    mean=non_nan_col.mean()
    col[np.isnan(col)]=mean



