ans = 0
n,d = map(int, input().split())
for i in range(n):
    x,y = map(int, input().split())
    ans += 1 if (x*x+y*y)**0.5 <= d else 0
print(ans)