#include <stdio.h>

struct edgelist
{
	int left;
	int right;
	int weight;
};
typedef struct edgelist edgelist;
edgelist edges[100];
int position;

struct union_struct
{
	int i;
	struct union_struct *top;
};
typedef struct union_struct unstr;
unstr un[100];
int unpos = 0;

void addedge();
void sort_edgelist();
void krus();
int is_same_set(int i);


int is_same_set(int i);

int main(){
	int i,j;
	for(int i=0;i<100;i++){
		un[i].i = i;
	}
	while(1){
		printf("Enter the case u want\n");
		scanf("%d",&i);
		switch(i){
			case 1:
				addedge();
				break;
			case 2:
				krus();
				break;
		}
	}
}

void addedge(){
	int a,b,w,i,j;
	printf("Enter the left and the right nodes\n");
	scanf("%d%d",&a,&b);
	printf("Enter the edge weight\n");
	scanf("%d",&w);
	edges[position].left = a;
	edges[position].right = b;
	edges[position].weight = w;
	position++;
}

void sort_edgelist(){
	for(int i = 0;i<position;i++){
		for(int j = i+1;j<position;j++){
			if(edges[i].weight>edges[j].weight){
				int temp;
				temp = edges[i].weight;
				edges[i].weight = edges[j].weight;
				edges[j].weight = temp;
				temp = edges[i].left;
				edges[i].left = edges[j].left;
				edges[j].left = temp;
				temp = edges[i].right;
				edges[i].right = edges[j].right;
				edges[j].right = temp;
			}
		}
	}
}

void krus(){
	int k,l;
	sort_edgelist();
	for(int i=0;i<position;i++){
		if(is_same_set(edges[i].left) != is_same_set(edges[i].right)){
			printf("%d  %d  %d\n",edges[i].left,edges[i].right,edges[i].weight);
			k = is_same_set(edges[i].right);
			l = is_same_set(edges[i].left);
			un[k].top = &un[l];
		}
	}
}

int is_same_set(int i){
	unstr *temp;
	if(un[i].top==NULL)
		return un[i].i;
	else{
		temp = un[i].top;
		while(temp->top!=NULL){
			temp = temp->top;
		}
		return temp->i;
	}
}