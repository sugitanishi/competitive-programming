#☆𝒐𝒎𝒂𝒋𝒊𝒏𝒂𝒊☆#
import sys
import math
from math import ceil, floor
import itertools
from functools import lru_cache
from collections import deque
inf=10**20
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()
'''''✂'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

n=int(input())
s=list(input())
ss=s[:]
ans_count=0

def check(n,sl):
    if n==0:
        return sl if sl>=2 else -1
    if n==1 and sl==1:
        return sl
    if n==1 and sl==0:
        return -1
    return check(n-1,sl//2)

word_len=check(n,len(s))
if word_len==-1:
    print('impossible')
    exit()

def f(st,en,q,i=0):
    global ss
    que=deque()
    que.append((st,en,q,i))
    if q==0:
        return
    while que:
        st,en,q,i=que.popleft()
        es=en-st
        if es==1:
            continue
        mid=(st+en)//2
        if es%2==1:
            ss[mid]=i
            if q-1!=0 and mid-st>1:
                que.appendleft((st,mid,q-1,i+1))
                que.appendleft((mid+1,en,q-1,i+1))
        else:
            if q-1!=0 and mid-st>1:
                que.appendleft((st,mid,q-1,i+1))
                que.appendleft((mid,en,q-1,i+1))

f(0,len(s),n)

memo={}
for i in range(len(s)):
    if type(ss[i])==int:
        if ss[i] in memo:
            if s[i] in memo[ss[i]]:
                memo[ss[i]][s[i]]+=1
            else:
                memo[ss[i]][s[i]]=1
        else:
            memo[ss[i]]={s[i]:1}

for v in memo.values():
    ans_count+=sum(v.values())-max(v.values())

i=0
words=[]
rev=False
while i<len(s):
    if rev:
        words.append(s[i:i+word_len][::-1])
    else:
        words.append(s[i:i+word_len])
    rev=not rev
    i=i+word_len
    if i>=len(s):
        break
    if type(ss[i])==int:
        i+=1

dd=[]
for i in range(word_len):
    used={'-':0,'$':0}
    for word in words:
        if word[i] in used:
            used[word[i]]+=1
        else:
            used[word[i]]=1
    used=sorted(used.items(),key=lambda x:-x[1])
    dd.append(((used[0][0],len(words)-used[0][1]),(used[1][0],len(words)-used[1][1]),(len(words)-used[1][1])-(len(words)-used[0][1])))

ans_s=[]
for ddd in dd:
    ans_s.append(ddd[0][0])
    ans_count+=ddd[0][1]

if ans_s!=ans_s[::-1] or len(ans_s)==1:
    print(ans_count)
else:
    mn=inf
    for i in range(len(ans_s)):
        if len(ans_s)%2==1 and i==len(ans_s)//2:
            continue
        mn=min(mn,dd[i][2])
    print(ans_count+mn)
