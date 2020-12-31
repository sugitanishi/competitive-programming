a,b = map(int, input().split())
c,d = map(int, input().split())

def ok(a, b, c, d):
    return a - b == c - d or \
        a + b == c + d or \
        abs(a - c) + abs(b - d) <= 3

if (a, b) == (c, d):
    print(0)
elif ok(a, b, c, d):
    print(1)
elif (a + b) % 2 == (c + d) % 2:
    print(2)
elif abs((a - b) - (c - d)) <= 3 or abs((a + b) - (c + d)) <= 3 or abs(a - c) + abs(b - d) <= 6:
    print(2)
else:
    print(3)