#include <stdio.h>

int m;
int min_finder(int key[m],int is_mat[m]);
int main(){
	int i,j;
	printf("Enter the number of nodes\n");
	scanf("%d",&m);
	int a[m][m];
	printf("Enter the adjcency matrix\n");
	for(i=0;i<m;i++){
		for(j = 0;j<m;j++){
			scanf("%d",&a[i][j]);
		}
	}
	int is_mat[m];
	int key[m];
	int parent[m];
	for(i = 0;i<m;i++){
		key[i] = 999;
		is_mat[i] = 0;
	}
	key[0] = 0;
	parent[0] = -1;
	for(i = 0;i<m-1;i++){
		int u = min_finder(key,is_mat);
		is_mat[u] = 1;
		for(int v = 0;v<m;v++){
			if(is_mat[v] == 0 && a[u][v]!=0 && a[u][v]<key[v]){
				key[v] = a[u][v];
				parent[v] = u;
			}
		}
	}
	for(i=1;i<m;i++){
		printf("%d  %d  %d\n",parent[i],i,a[i][parent[i]] );
	}
}

int min_finder(int key[],int is_mat[]){
	int min = 999;
	int min_ind;
	for(int i = 0;i<m;i++){
		if(is_mat[i] == 0 && key[i]<min){
			min = key[i];
			min_ind = i;
		}
	}
	return min_ind;
}