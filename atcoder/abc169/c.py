a,b=input().split()
c=1
if '.' in b:
  c = len(b)-b.index('.')
  b=b.replace('.','')
a,b=int(a),int(b)
print(a*b*10//(10**c))