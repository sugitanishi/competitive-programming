x,k,d=map(int,input().split())
    
def solve(x,k,d):
    x = abs(x)
    a,b = x-x//(2*d)*(2*d),x-x//(2*d)*(2*d)-2*d
    ideal = a if abs(a)<=abs(b) else b
    count = (x-ideal)//d
    return abs(x-min(count,k)*d)

print(solve(x,k,d) if k%2==0 else min(solve(x+d,k-1,d),solve(x-d,k-1,d)))
