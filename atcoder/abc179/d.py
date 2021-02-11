import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

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
        ans=0
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

n,k=map(int,input().split())
d=[]
for i in range(k):
    a,b=map(int,input().split())
    d.append((a,b))

st=SegTree(n,0,lambda x,y:x+y)
st.update(0,1,lambda x,y:y)
for i in range(1,n):
    tmp=0
    for j in range(k):
        l,r=d[j]
        if i-l>=0:
            tmp+=st.find(max(i-r,0),i-l)
    st.update(i,tmp,lambda x,y:y%998244353)
print(st.data()[n-1])
