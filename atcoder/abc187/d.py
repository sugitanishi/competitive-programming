import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

n=int(input())
d=[]
aoki=0
takahashi=0
for i in range(n):
    a,b=map(int,input().split())
    d.append((a,b))
    aoki+=a
d=sorted(d,key=lambda x:-(x[0]+x[0]+x[1]))
count=0
for a,b in d:
    aoki-=a
    takahashi+=a+b
    count+=1
    if aoki<takahashi:
        print(count)
        break

