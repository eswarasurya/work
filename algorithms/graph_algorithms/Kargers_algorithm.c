#include<stdio.h>
#include<stdlib.h>
#include<time.h>

struct edge_list
{
	int left;
	int right;
};
typedef struct edge_list edge_list;


int n,e;
int set_num(int a[]);
int main(){
	int i,j,k;
	printf("Enter the number of edges\n");
	scanf("%d",&e);
	printf("Entre the number of nodes\n");
	scanf("%d",&n);
	int a[n];
	for(int i = 0;i<n;i++){
		a[i] = i;
	}
	printf("Enter the left and right nodes of the edges\n");
	edge_list edges[e];
	for(i = 0;i<e;i++){
		scanf("%d %d",&edges[i].left,&edges[i].right);
	}
	
	while(set_num(a)>2){
		int r = rand()%e;
		if(a[edges[r].left] == a[edges[r].right]){
			continue;
		}
		a[edges[r].left] = a[edges[r].right];
	}
	int p,q;
	p = a[0];
	for(int i = 0;i<n;i++){
		if(a[i]!=p)
			q = a[i];
	}
	int count = 0;
	for(int i = 0;i<e;i++){
		if(a[edges[i].left] != a[edges[i].right]){
			count++;
		}
	}
	printf("Number of edges that were cut by kargers algorithm: %d\n", count);
}

int set_num(int a[]){
	int count = 0;
	int b[n];

	for(int i = 0;i<n;i++){
		b[i] = 0;
	}
	for(int i = 0;i<n;i++){
		b[a[i]]++;
	}
	for(int i = 0;i<n;i++){
		if(b[i]>0)
			count++;
	}
	return count;
}