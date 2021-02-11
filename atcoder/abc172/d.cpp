#include <bits/stdc++.h>
using namespace std;
 
int main(void){
    long long a[10000001]={0},i,j,n,ans=0;
    cin>>n;
    for(i=1;i<10000001;i++) for(j=i;j<10000001;j+=i) a[j]++;
    for(i=1;i<=n;i++) ans+= i*a[i];
    cout<<ans<<endl;
}