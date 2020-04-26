#include<stdio.h>
#include<stdlib.h>

struct node
{
    int i;
    struct node *neighbour;
    struct node *child;
    int is_visited;
    int start_time;
    int end_time;
    int level;
};

typedef struct node node;
node *root = NULL;

struct q
{
    node *ptr;
    struct q *next;
};

typedef struct q q;
q *head = NULL;

void print_list(node *temp);
void addnode(int val);
node *find_node(int val);
void addedge(int e1, int e2);
void dfs(node *ptr);
void node_zero(node *temp);
void print_time();
void enque(node *temp);
q* dequeu();
void bfs();

int time = 0;


int main()
{
    int i,j,k,e1,e2;
    printf("\nAdjcency list implementation of an undirected graph\n");
    printf("1. Inserting a Node\n2. Adding edge");
    printf("3. Printing Adjcency list\n4. DFS\n5. BFS\n\n");
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
            break;
        case 2:
            printf("Enter the two nodes of the edge\n");
            scanf("%d%d",&e1,&e2);
            addedge(e1,e2);
            break;
        case 3:
            printf("Printing Adjcency list\n");
            print_list(root);
            break;
        case 4:
            printf("DFS\n");
            time = 0;
            node_zero(root);
            dfs(root);
            print_time();
            break;
        case 5:
            printf("BFS\n");
            time = 0;
            node_zero(root);
            enque(root);
            bfs();
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
    temp->is_visited = 0;
    temp->start_time = 0;
    temp->end_time = 0;
    temp->level = 0;
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

void addedge(int e1, int e2)
{
    node *temp,*temp1,*p1,*p2;
    p1 = (node*)malloc(sizeof(node));
    p2 = (node*)malloc(sizeof(node));
    p1->i = e1;
    p2->i = e2;
    temp = find_node(e1);

    while(temp->child!=NULL)
    {
        temp = temp->child;
    }
    temp->child = p2;
    temp1 = find_node(e2);

    while(temp1->child!=NULL)
    {
        temp1 = temp1->child;
    }
    temp1->child = p1;
}

node *find_node(int val)    //Returns the node
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
    printf("%d",temp1->i);
    temp1 = temp1->child;
    while(temp1!=NULL)
    {
        printf("->%d",temp1->i);
        temp1 = temp1->child;
    }
    printf("\n");
    print_list(temp->neighbour);
}

void node_zero(node *temp)  //Makes the time zero
{
    node *temp1;
    if(temp==NULL)
        return;

    temp1 = temp;

    while(temp1!=NULL)
    {
        temp1->is_visited = 0;
        temp1->start_time = 0;
        temp1->end_time = 0;
        temp1 = temp1->child;
    }

    node_zero(temp->neighbour);
}

void dfs(node *ptr)
{
    if(ptr == NULL)
        return;

    node *temp, *temp1, *temp2;
    temp = find_node(ptr->i);
    temp2 = temp;
    if(temp->is_visited == 1)
        return;

    printf("%d ",temp->i );
    temp->is_visited = 1;
    temp->start_time = time;
    if(temp->child == NULL)
        return;

    time++;
    while(temp!=NULL)
    {
        dfs(temp->child);
        temp = temp->child;
    }
    temp2->end_time = time;
    time++;
}

void print_time()
{
    node *temp;
    temp = root;
    while(temp != NULL)
    {
        printf("\nNode %d Start time %d End Time %d",temp->i,temp->start_time,temp->end_time);
        temp = temp->neighbour;
    }
    printf("\n");
}

void bfs()
{
    q *ptr1,*t;
    ptr1 = head;
    node *temp,*temp1,*temp2;
    int lev;
    while(ptr1!=NULL)
    {
        temp = ptr1->ptr;
        temp1 = find_node(temp->i);
        lev = temp1->level;
        temp1->is_visited = 1;
        temp1 = temp1->child;
        while(temp1!=NULL)     
        {
            temp2 = find_node(temp1->i);
            
            if(temp2->is_visited!=1)
            {   
                temp2->level = lev+1;
                enque(temp2);
                temp2->is_visited = 1;
            }
            temp1 = temp1->child;
        }
        if(dequeu==NULL)
            return;

        t = dequeu();
        printf("Node: %d  Depth: %d\n",t->ptr->i,t->ptr->level);
        ptr1 = ptr1->next;
    }
}

void enque(node *temp)  //Adds a new element at the end of the linked list
{
    q *temp1;
    q *new_node;
    new_node = (q*)malloc(sizeof(q));
    new_node->ptr = temp;
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

