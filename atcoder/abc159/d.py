import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

n=int(input())
a=list(map(int,input().split()))
dic={}
for x in a:
    if x in dic:
        dic[x]+=1
    else:
        dic[x]=1
ans=0
for key in dic:
    ans += dic[key]*(dic[key]-1)//2
    dic[key]=dic[key]*(dic[key]-1)//2,(dic[key]-1)*(dic[key]-2)//2

for i in range(n):
    print(ans-dic[a[i]][0]+dic[a[i]][1])
