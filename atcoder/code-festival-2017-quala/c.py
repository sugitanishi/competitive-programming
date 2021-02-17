# coding: utf-8
h,w=map(int,input().split())
dic={}
for i in range(h):
    for c in input():
        if c in dic:
            dic[c]=(dic[c]+1)%4
        else:
            dic[c]=1
d=list(dic.values())
if h%2 and w%2:
    if d.count(1)+d.count(3)==1 and d.count(2)<=h//2+w//2:
        print('Yes')
    else:
        print('No')
elif (h%2 and not w%2) or (w%2 and not h%2):
    if not (d.count(1)+d.count(3)>0):
        if h%2:
            if d.count(2)<=w//2 :#and d.count(2)%2==(w//2)%2:
                print('Yes')
            else:
                print('No')
        elif w%2:
            if d.count(2)<=h//2 :#and d.count(2)%2==(h//2)%2:
                print('Yes')
            else:
                print('No')
    else:
        print('No')
else:
    if sum(d)==0:
        print('Yes')
    else:
        print('No')