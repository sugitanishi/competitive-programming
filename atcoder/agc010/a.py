n=int(input())
print('YES' if len(list(filter(lambda x:x%2==1,map(int,input().split()))))%2==0 else 'NO')