#include<stdio.h>
int main() {
    int n,i,j,cnt=0,q,val;
    scanf("%d",&n);
    int arr[n],arr1[n];
    for(i=0;i<n;i++){
        scanf("%d",&arr[i]);
        arr1[i]=cnt+arr[i];
        cnt+=arr[i];
    }
    int max=arr1[n-1];
    //printf("%d",max);
    scanf("%d",&q);
    for(j=0;j<q;j++){
        cnt=1;
        scanf("%d",&val);
        if(val>max){
            printf("%d\n",-1);
        }
        else{
        for(i=0;i<n;i++){
            if(arr1[i]<val){
                cnt+=1;
            }
            else{
                printf("%d\n",cnt);
                break;
            }
        }
        }
    }   
    return 0;
}
