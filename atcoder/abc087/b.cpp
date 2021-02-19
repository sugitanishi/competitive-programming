#include <bits/stdc++.h>
using namespace std;
int main(void){
    int x,a,b,c;
    cin>>a>>b>>c>>x;
    int i,j,k,ans=0;
    for(i=0;i<=a;i++){
        for(j=0;j<=b;j++){
            for(k=0;k<=c;k++){
                ans+=(i*500+j*100+k*50)==x;
            }
        }
    }
    cout<<ans<<endl;
}
