#while循环
# while True:#死循环
#     print("a")
#用程序去数数，从1~100
# i=1
# while i<=100:
    # print(i)
    # i=i+1
#1+......100
i=1
s=0
while i<=100:
    s=s+i#累加
    i=i+1
print(s)
#1-2+3-4+5....-100
n=1
s=0

while n<=99:
   s=s+n
   n=n+2
a=-2
b=0
while a>=-100:
    b=b+a
    a=a-2
print(s+b)
j=1
k=0
while j<=100:
    if(j%2==0):
        k-=j
    else:
        k+=j
    j+=1
print(k)
