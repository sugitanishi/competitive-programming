import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

def divisors(n):
    d = []
    i = 1
    while i*i <= n:
        if n % i == 0:
            d.append(i)
            if n//i != i:
                d.append(n//i)
        i += 1
    return sorted(d)

n = int(input())
p = sum(divisors(n))-n
if n == p:
    print('Perfect')
elif n < p:
    print('Abundant')
else:
    print('Deficient')
