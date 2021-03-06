#include<stdio.h>
#include<stdlib.h>

struct node
{
    int i;
    struct node *neighbour;
    struct node *child;
    int weight;
    int distance;
};

typedef struct node node;
node *root = NULL;

void addnode(int val);
void addedge(int e1, int e2, int w);
node *find_node(int val);
void print_list(node *temp);
void bellman();
int node_count = 0;

int main()
{
    int i,j,k,e1,e2,w;
    printf("\nAdjcency list implementation of an directed graph\n");
    printf("1. Inserting a Node\n2. Adding edge");
    printf("3. Print Adjcency list\n4. Bellman_Ford Algorithm\n");
    while(1)
    {
        printf("Enter the case u want\n");
        scanf("%d",&k);
        switch(k)
        {
        case 1:
            printf("Enter the value of the node\n");
            scanf("%d",&i);
            addnode(i);
            node_count++;
            break;
        case 2:
            printf("Enter the two nodes of the edge \n");
            scanf("%d%d",&e1,&e2);
            printf("Enter the weight of the edge\n");
            scanf("%d",&w);
            addedge(e1,e2,w);
            break;
        case 3:
            printf("Printing Adjcency list\n");
            print_list(root);
            break;
        case 4:
        	bellman();
        	break;
        default:
            exit(1);
        }
    }
}


void addnode(int val)
{
    int i,j,k;
    node *temp,*temp1;
    temp = (node*)malloc(sizeof(node));
    temp->i = val;
    temp->neighbour = NULL;
    temp->child = NULL;
    if(node_count == 0){
    	temp->distance = 0;
    }
    else
    	temp->distance = 999;  //considering 999 as infinite
    temp->weight = 0;
    if(root == NULL)
    {
        root = temp;
    }
    else
    {
        temp1 = root;
        while(temp1->neighbour!=NULL)
        {
            temp1 = temp1->neighbour;
        }
        temp1->neighbour = temp;
    }
}

void addedge(int e1, int e2, int w)
{
    node *temp,*temp1,*p1,*p2;
    p2 = (node*)malloc(sizeof(node));
    p2->i = e2;
    p2->weight = w;
    temp = find_node(e1);

    while(temp->child!=NULL)
    {
        temp = temp->child;
    }
    temp->child = p2; 
}

node *find_node(int val)    
{
    node *temp;
    temp = root;
    while(temp->i!=val)
    {
        temp = temp->neighbour;
    }
    return temp;
}

void print_list(node *temp)
{
    node *temp1;
    if(temp==NULL)
        return;
    temp1 = temp;
    printf("%d(dist %d)",temp1->i,temp1->distance);
    temp1 = temp1->child;
    while(temp1!=NULL)
    {
        printf("->%d(%d)",temp1->i,temp1->weight);
        temp1 = temp1->child;
    }
    printf("\n");
    print_list(temp->neighbour);
}


void bellman(){
	node *ptr = root;
	node *temp,*temp1;
	int i,j,k,p,q;
	for(int i=0;i<node_count;i++){
		ptr = root;
		while(ptr!=NULL){
			temp = ptr->child;
			while(temp!=NULL){
				temp1 = find_node(temp->i);
				if(temp1->distance>ptr->distance+temp->weight)
				{
					temp1->distance = ptr->distance+temp->weight;
				}
				temp = temp->child;
			}
			ptr = ptr->neighbour;
		}
	}

	ptr = root;
	while(ptr->neighbour!=NULL){
			temp = ptr->child;
			while(temp!=NULL){
				temp1 = find_node(temp->i);
				if(temp1->distance>ptr->distance+temp->weight)
				{
					printf("The graph has a negeative cycle\n");
					break;
				}
				temp = temp->child;
			}
			ptr = ptr->neighbour;
		}


}