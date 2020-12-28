import sys
sys.setrecursionlimit(10000000)
input=lambda:sys.stdin.readline().rstrip()

def cmp(a,b):
    ret=0
    for i in range(len(a)):
        if a[i]!=b[i]:
            ret+=1
    return ret

def line_up(a,b):
    a=a[:]
    b=b[:]
    ret=['0' for i in range(len(a))]
    for i in range(len(a)):
        try:
            del b[b.index(a[i])]
            ret[i]=a[i]
        except:
            continue
    b=sorted(b)[::-1]
    for i in range(len(a)):
        if ret[i]=='0':
            ret[i]=b.pop()
    return ret
        

n,m=map(int,input().split())
s=list(input())
ss=sorted(s)

ans = ''
cost=0
for i in range(n):
    for j in range(len(ss)):
        if cmp(s[i+1:],line_up(s[i+1:],ss[:j]+ss[j+1:]))+cost+int(s[i]!=ss[j])<=m:
            ans+=ss[j]
            if s[i]!=ss[j]:
                cost+=1
            del ss[j]
            break
print(ans)
