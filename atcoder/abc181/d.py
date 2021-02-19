import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

s=input()
if len(s)==1:
    print('Yes' if s=='8' else 'No')
    exit()
if len(s)==2:
    a,b=s
    print('Yes' if int(a+b)%8==0 or int(b+a)%8==0  else 'No')
    exit()

check=[str(x) for x in range(104,1000,8) if '0' not in str(x)]
dic={c:0 for c in '123456789'}
for c in s: 
    dic[c]+=1

for check_str in check:
    for c in '123456789':
        if check_str.count(c)>dic[c]:
            break
    else:
        print('Yes')
        break
else:
    print('No')