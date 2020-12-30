import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

class UnionFind:
    def __init__(self, n):
        self.data=[-1 for i in range(n)]

    def root(self,x):
        if self.data[x]<0:
            return x
        else:
            self.data[x]=self.root(self.data[x])
            return self.data[x]

    def uni(self,x,y):
        x=self.root(x)
        y=self.root(y)
        if(x==y):
            return
        if self.data[y]<self.data[x]:
            x,y=y,x
        self.data[x]+= self.data[y]
        self.data[y] = x

    def same(self,x,y):
        return self.root(x)==self.root(y)

    def size(self,x):
        return -self.data[self.root(x)]

nums = list('0987654321')
alps = list('QWERTYUIOPASDFGHJKLZXCVBNM')
n = int(input())
a,b = list(input()),list(input())
used_c = set()

for i in range(n):
    if a[i] in alps:
        used_c.add(a[i])
    if b[i] in alps:
        used_c.add(b[i])

uf = UnionFind(len(alps))
al_num = {}
for i in range(n):
    if a[i] in nums and b[i] in nums:
        continue
    if a[i] in alps and b[i] in nums:
        al_num[a[i]] = b[i]
        continue
    if b[i] in alps and a[i] in nums:
        al_num[b[i]] = a[i]
        continue
    uf.uni(alps.index(a[i]), alps.index(b[i]))

del_set = set()
list_used_c = list(used_c)
for i in range(len(used_c)):
    if list_used_c[i] in al_num:
        del_set.add(list_used_c[i])
    for j in range(i+1, len(used_c)):
        if list_used_c[i] != list_used_c[j] and uf.same(alps.index(list_used_c[i]), alps.index(list_used_c[j])):
            del_set.add(list_used_c[j])
            if list_used_c[j] in al_num:
                del_set.add(list_used_c[i])

used_c -= del_set
ans = 1
for c in used_c:
    if c == a[0] or c == b[0]:
        ans *= 9
    else:
        ans *= 10
print(ans)
