import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

def db(x,y,mod):
    if x==1:
        return 1
    dbdb=[x%mod]
    mx=y
    i=2
    while True:
        if i<=mx:
            dbdb.append(dbdb[-1]**2)
            i*=i
        else:
            break
    ans=1
    for i in range(len(dbdb)):
        if y&(1<<i):
            ans=ans*dbdb[i]%mod
    return ans

a,b,c=map(int,input().split())
xa=a%10
d=[a%10]
aa=xa
for i in range(10):
    aa*=xa
    if aa%10 not in d:
        d.append(aa%10)
    else:
        break
mod=len(d)
print(d[db(b,c,mod)-1])