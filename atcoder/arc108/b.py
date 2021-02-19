import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

n=int(input())
s=input()
while True:
    p=s.find('fox')
    if p==-1:
        break
    l=3
    while True:
        if 0<=p-1<=p+l+2<=len(s) and s[p-1]+s[p+l:p+l+2]=='fox':
            p=p-1
            l+=3
            continue
        elif 0<=p-2<=p+l+1<=len(s) and s[p-2:p]+s[p+l]=='fox':
            p=p-2
            l+=3
            continue
        else:
            break
    s=s.replace(s[p:p+l],'')
print(len(s))