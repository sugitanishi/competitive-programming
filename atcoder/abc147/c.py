import sys
sys.setrecursionlimit(10000000)
input=lambda:sys.stdin.readline().rstrip()

n=int(input())
data=[[] for i in range(n)]
for i in range(n):
    for j in range(int(input())):
        a,b=map(int,input().split())
        data[i].append((a-1,b))

ans=0
for bit in range(2**(n)):
    count=0
    for i in range(n):
        if bit&(1<<i):
            count+=1
            ok=True
            for a,b in data[i]:
                if bool(bit&(1<<a))!=bool(b):
                    ok=False
                    break
            if not ok:
                break
    else:
        ans=max(ans,count)
print(ans)
