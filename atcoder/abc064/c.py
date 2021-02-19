dic={}
n=int(input())
data=list(map(int,input().split()))
ans=0
for i in range(n):
    if data[i]>3199:
        ans+=1
    elif data[i]//400 not in dic:
        dic[data[i]//400]=1
if len(dic)==0:
    print(1,ans)
else:
    print(len(dic),ans+len(dic))
