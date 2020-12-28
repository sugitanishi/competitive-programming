import sys
sys.setrecursionlimit(10000000)
input=lambda:sys.stdin.readline().rstrip()

import bisect
n,t=map(int,input().split())
a=list(map(int,input().split()))
left=a[:len(a)//2]
right=a[len(a)//2:]

left_s=set([0])
for x in left:
    left_s|={x+y for y in left_s}

right_s=set([0])
for x in right:
    right_s|={x+y for y in right_s}

left_a=sorted(left_s)
right_a=list(right_s)

ans=0
for right_num in right_a:
    if right_num>t:
        continue
    ans=max(ans,right_num+left_a[bisect.bisect_right(left_a,t-right_num)-1])
print(ans)