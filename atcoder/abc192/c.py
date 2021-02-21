import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

def f(x):
    a=sorted(str(x))
    b=sorted(str(x),reverse=True)
    return int(''.join(b)) - int(''.join(a))

n,k=map(int,input().split())
for i in range(k):
    n=f(n)
print(n)
