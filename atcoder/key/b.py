n,k = map(int,input().split())
a = sorted(list(map(int,input().split())))

d1 = [0 for i in range(3*(10**5) + 2)]
d2 = [[] for i in range(3*(10**5) + 2)]
for i in range(n):
    d1[a[i]] += 1
for i in range(len(d1)):
    d2[d1[i]].append(i)

tmp = 999999999999999
ans = 0
for i in range(k):
    if len(d2[i]) == 0:
        ans += tmp
        continue
    if d2[i][0]<tmp:
        tmp = d2[i][0]
        ans += d2[i][0]
    else:
        ans += tmp
print(ans)
