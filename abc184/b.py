n,x=map(int,input().split())
s=input()
for c in s:
    if c=='x':
        x=max(x-1,0)
    else:
        x+=1
print(x)