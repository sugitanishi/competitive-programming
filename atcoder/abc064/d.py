n=int(input())
data=list(map(lambda x:[str(x),-1],input()))
while 1:
    i=0
    while i<len(data):
        if data[i][0]==')' and data[i][1] == -1:
            break
        i+=1
    if i==len(data):
        break
    j=i-1
    while j>=0:
        if data[j][0]=='(' and data[j][1]==-1:
            data[i][1]=1
            data[j][1]=1
            break
        j-=1
    if j==-1:
        data[i][1]=1
        data.insert(0,['(',1])
while 1:
    i=len(data)-1
    while i>=0:
        if data[i][0]=='(' and data[i][1] == -1:
            break
        i-=1
    if i==-1:
        break
    data[i][1]=1
    data.append([')',1])
print(''.join(list(map(lambda x:x[0],data))))