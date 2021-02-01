import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

from itertools import accumulate
h,w,c=map(int,input().split())
field=[list(map(int,str(input()))) for i in range(h)]
acm_field=[list(accumulate(field[i])) for i in range(h)]

def slice_check(h1,w1,h2,w2,c):
    count = 0
    for i in range(h1,h2):
        count += acm_field[i][w2-1] - (acm_field[i][w1-1] if w1-1>=0 else 0)
    return c>=count

ans = 99999999999
for i in range(2**(h-1)):
    cut_h=[-1]
    for j in range(h-1):
        if i & (1<<j):
            cut_h.append(j)
    cut_h.append(h-1)
    cut_w=[-1]
    k=0
    ff=True
    while k<w:
        f=False
        for j in range(len(cut_h)-1):
            if not slice_check(cut_h[j]+1,cut_w[-1]+1,cut_h[j+1]+1,k+1,c):
                cut_p=k-1
                break
        else:
            f=True
        if f:
            k+=1
            continue
        if cut_p!=cut_w[-1]:
            cut_w.append(cut_p)
        else:
            ff=False
            break
    if ff:
        ans=min(ans,len(cut_h)+len(cut_w)-3)
print(ans)