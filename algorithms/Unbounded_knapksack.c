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
	int k[weight+2];
	int items[weight+2][weight+2];
	int indexes[weight+2];
	for(int i = 0;i<weight+2;i++){
		indexes[i] = 0;
	}

	k[0]=0;
	for(int x = 1;x<=weight+1;x++){
		k[x] = 0;
		for(int i = 1;i<=n;i++){
			if(w[i]<x){
				int p = k[x];
				k[x] = find_max(k[x],k[x-w[i]]+v[i]);
				if(p!=k[x]){
					indexes[x] = 0;
					for(int l = 0;l<indexes[x-w[i]];l++){
						items[x][indexes[x]] = items[x-w[i]][l];
						indexes[x]++;
					}
					items[x][indexes[x]] = w[i];
					indexes[x]++;
				}
			}
		}
	}
	printf("Max capacity of knapsack: %d\n",k[weight+1] );
	printf("Items in the knapsack are of following weights: ");
	for(int i = 0;i<indexes[weight+1];i++){
		printf("%d ",items[weight+1][i] );
	}
}

int find_max(int a,int b){
	if(a>b)
		return a;
	else
		return b;
}