n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

mx_a = 0
mx_ab = 0
for i in range(n):
    mx_a = max(mx_a, a[i])
    mx_ab = max(mx_a*b[i], mx_ab)
    print(mx_ab)
