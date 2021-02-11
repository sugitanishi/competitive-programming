import sys
sys.setrecursionlimit(10000000)
input=lambda:sys.stdin.readline().rstrip()
 
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
st=SegTree(3000001,0,max)
[(lambda x:st.update(x,st.find(max(x-k,0),min(x+k,3000001))+1,lambda a,b:b))(int(input())) for i in range(n)]
print(st.find(0,3000001))