import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

n=int(input())
p=list(map(int,input().split()))
def solve(p):
    count=0
    for i in range(len(p)-1):
        if p[i]==i+1:
            p[i],p[i+1]=p[i+1],p[i]
            count+=1
    if p[-1]==len(p):
        count+=1
    return count

print(solve(p))
