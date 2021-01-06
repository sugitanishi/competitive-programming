def prime_factor(n):
    x=2
    lim=int(n**0.5)
    factors=[]
    while n!=1 and x<=lim:
        if n%x==0:
            n//=x
            factors.append(x)
        else:
            x+=1
    if n!=1:
        factors.append(n)
    return factors

n=int(input())
pf = prime_factor(n)
spf = sorted(set(pf))
counts = []
for x in spf:
    counts.append(pf.count(x))

ans = 0
for count in counts:
    l = count
    for i in range(1,l+1):
        if count - i >= 0:
            ans+=1
            count-=i
        else:
            break
print(ans)