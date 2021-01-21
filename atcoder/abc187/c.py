s = set([input() for i in range(int(input()))])
for c in s:
  if c.startswith('!'):
    continue
  if '!'+c in s:
    print(c)
    break
else:
  print('satisfiable')