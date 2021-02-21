#include <iostream>
using namespace std;
int main(void){
    int k;
    long long ans=0;
    cin>>k;
    ans=0;
    for(int i=1;i<=k;i++){
        for(int j=1;j<=k/i;j++){
            ans+=k/i/j;
        }
    }
    cout<<ans<<endl;
}
