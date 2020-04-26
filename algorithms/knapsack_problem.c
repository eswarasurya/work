#include<stdio.h>

int find_max(int a,int b);
int main(){
	int n,weight;
	printf("Enter no of items\n");
	scanf("%d",&n);

	int w[n+1],v[n+1];
	printf("Enter weights and values\n");
	for(int i = 1;i<=n;i++){
		scanf("%d %d",&w[i],&v[i]);
	}

	printf("Enter the weight of the knapsack\n");
	scanf("%d",&weight);
	int k[weight+1][n+1];
	for(int i = 0;i<weight+1;i++){
		k[i][0] = 0;
	}
	for(int i = 0;i<n+1;i++){
		k[0][i] = 0;
	}
	for(int x = 1;x<=weight;x++){
		for(int j = 1;j<=n;j++){
			k[x][j] = k[x][j-1];
			if(w[j]<=x){
				k[x][j] = find_max(k[x][j],k[x-w[j]][j-1] + v[j]);
			}
		}
	}
	printf("Max capacity of knapsack: %d\n",k[weight][n]);
}

int find_max(int a,int b){
	if(a>b)
		return a;
	else
		return b;
}