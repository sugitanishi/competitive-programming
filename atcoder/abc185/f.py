#☆𝒐𝒎𝒂𝒋𝒊𝒏𝒂𝒊☆#
import sys
import math
from math import ceil, floor
import itertools
from functools import lru_cache
from collections import deque
inf=10**20
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()
'''''✂'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

class SegTree:
    '''Segment Tree:
    Data structure to answer queries on segments of a sequence.
    '''
    def __init__(self,n,init_num,func):
        '''Create a segment tree.
        :param n: Size
        :type n: int or float (number)
        :param init_num: Initialization number
        :type init_num: int or float (number)
        :param func: Function to use
        :type func: function
        '''
        self.func=func
        self.init_num=init_num
        self.size = 2**(len(bin(n-1))-2)*2-1
        self.tree = [init_num for i in range(self.size)]
     
    def data(self):
        '''Return data.
        '''
        return self.tree[self.size//2:]
 
    def update(self,i,x,update_func):
        '''Update the i-th data by update_func.
            example:
            a[i]<-update_func(a[i],x)
        '''
        i=self.size//2+i
        self.tree[i]=update_func(self.tree[i],x)
        while 1:
            i=(i-1)//2
            self.tree[i]=self.func(self.tree[i*2+1],self.tree[i*2+2])
            if i<=0:
                break
 
    def find(self,s,t):
        '''Answer query on [s,t]segment
        '''
        ans=self.init_num
        l,r=s+self.size//2,t+self.size//2+1
        while(l<r):
            if l%2==0:
                ans=self.func(ans,self.tree[l])
            l//=2
            if r%2==0:
                ans=self.func(ans,self.tree[r-1])
                r-=1
            r//=2
        return ans

n,q=map(int,input().split())
a=list(map(int,input().split()))
st=SegTree(n, 0, lambda x,y:x^y)

for i in range(n):
    st.update(i,a[i],lambda p,q:q)

for i in range(q):
    t,x,y=map(int,input().split())
    if t==1:
        st.update(x-1,y,lambda p,q:p^q)
    else:
        print(st.find(x-1,y-1))

