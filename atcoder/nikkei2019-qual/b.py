# coding: utf-8
n=int(input())
a,b,c=input(),input(),input()
count=0
for i in range(n):
    s=set([a[i],b[i],c[i]])
    if len(s)==3:
        count+=2
    elif len(s)==2:
        count+=1
print(count)