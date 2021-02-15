n=int(input())
log=[]
H=[]
for i in range(n):
    log.append(tuple(map(int,input().split())))
t,a=1,1
for x,y in log:
    nxt=max(t//x + (1 if t%x else 0),a//y + (1 if a%y else 0))
    t=x*nxt
    a=y*nxt
print(t+a)