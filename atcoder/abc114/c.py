import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

n=input()
count=0
def check(n,s):
    if len(s)>len(n):
        return
    global count
    if int(s)<=int(n) and len(set(s))==3:
        count+=1
    check(n,'3'+s),check(n,'5'+s),check(n,'7'+s)
    return
check(n,'3'),check(n,'5'),check(n,'7')
print(count)