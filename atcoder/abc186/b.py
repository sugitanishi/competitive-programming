h,w=map(int,input().split())
mn=9999999999999
sm=0
for i in range(h):
  a=list(map(int,input().split()))
  mn=min(mn,min(a))
  sm+=sum(a)
print(sm-mn*h*w)