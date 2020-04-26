#include<stdio.h>
#include<stdlib.h>

struct q
{
    int i;
    struct q *next;
};

typedef struct q q;
q *head = NULL;	

int n;

q* dequeu();
void enque(int i) ;
int min(int a, int b);
int BFS(int res[n][n], int parent[]);
int isempty();



int main(){
	int i,j,k;
	printf("Enter the number of nodes\n");
	scanf("%d",&n);
	int a[n][n];
	printf("Enter the matrix\n");
	
	for(i = 0;i<n;i++){
		for(j = 0;j<n;j++){
			scanf("%d",&a[i][j]);
			// res[i][j] = a[i][j];
		}
	}
	int u;
	int res[n][n];
	int parent[n];
	int max_flow = 0;

	for(int i = 0;i<n;i++){
		for(int j = 0;j<n;j++){
			res[i][j] = a[i][j];
		}
	}
	while(BFS(res,parent) == 1){
		int min_edge = 999;
		for(i = n-1;i!=0;i = parent[i]){
			u = parent[i];
			min_edge = min(min_edge, res[u][i]);
		}

		for(i = n-1;i!=0;i = parent[i]){
			u = parent[i];
			res[u][i] -= min_edge;
			res[i][u] += min_edge;
		}
		max_flow = max_flow + min_edge;
	}

	printf("Answer : %d\n",max_flow );

}

int min(int a,int b){
	if(a>b)
		return b;
	else
		return a;
}

int BFS(int res[n][n], int parent[n]){
	int visited[n];
	head = NULL;
	for(int i = 0;i<n;i++){
		visited[i] = 0;
	}	
	 enque(0);
	 visited[0] = 1;
	 parent[0] = -1;
	 while(isempty() == 0){
	 	q *temp = dequeu();
	 	int k = temp->i;
	 	for(int i = 0;i<n;i++){
	 		if(visited[i] == 0 && res[k][i] > 0){
	 			enque(i);
	 			parent[i] = k;
	 			visited[i] = 1;
	 		}
	 	}
	 }
	 return visited[n-1];
}

void enque(int i)  //Adds a new element at the end of the linked list
{
    q *temp1;
    q *new_node;
    new_node = (q*)malloc(sizeof(q));
    new_node->i = i;
    new_node->next = NULL;
    if(head == NULL)
    {
        head = new_node;
    }
    else
    {
        temp1 = head;
        while(temp1->next!=NULL)
        {
            temp1 = temp1->next;
        }
        temp1->next = new_node;
    }
}

q* dequeu() //Returns the first element of the linked list
{
    if(head == NULL)
        return NULL;
    q *temp;
    temp = head;
    head = head->next;
    return temp;
}

int isempty(){
	if(head == NULL){
		return 1;
	}
	else{
		return 0;
	}
}
