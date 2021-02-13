import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

k=int(input())
luns=list(map(str,range(1,10)))
start=0
p=0
while len(luns)>p:
    for j in range(max(int(luns[p][-1])-1,0),min(int(luns[p][-1])+2,10)):
        if int(luns[p]+str(j))<=3234566667:
            luns.append(luns[p]+str(j))
    p+=1
print(luns[k-1])
