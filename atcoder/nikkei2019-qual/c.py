# coding: utf-8
n=int(input())
data=[]
for i in range(n):
    data.append(list(map(int,input().split())))
data=sorted(data,key=lambda x:-x[0]-x[1])
a=0
b=0
for i in range(n):
    if i%2==0:
        a+=data[i][0]
    else:
        b+=data[i][1]
print(a-b)