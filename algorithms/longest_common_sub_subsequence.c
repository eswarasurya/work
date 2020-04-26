#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int find_max(int a,int b);
int main(){
	char x[20],y[20];
	printf("Enter the first secquence\n");
	fflush(stdin);
	scanf("%s",x);
	printf("Enter the second secquence\n");
	fflush(stdin);		
	scanf("%s",y);
	int p = (int)strlen(x);
	int q = (int)strlen(y);
	int a[p+1][q+1];
	for(int i = 0;i<=p;i++){
		a[i][0] = 0;
	}
	for(int i = 0;i<=q;i++){
		a[0][i] = 0;
	}
	for(int i = 1;i<=p;i++){
		for(int j = 0;j<=q;j++){
			if(x[i-1] == y[j-1]){
				a[i][j] = a[i-1][j-1]+1;
			}
			else{
				a[i][j] = find_max(a[i][j-1],a[i-1][j]);
			}
		}
	}
	printf("\nMax sub secquence is: %d\n",a[p][q] );
	int i = p;
	int j = q;
	char str[20];
	int strind = 0;
	while(1){
		if(i<1 || j<1)
			break;
		if(x[i-1] == y[j-1]){
			str[strind] = x[i-1];
			strind++;
			i = i-1;
			j = j-1;
		}
		else{
			if(a[i][j] == a[i][j-1])
				j = j-1;
			else if(a[i][j] == a[i-1][j]){
				i = i-1;
			}
		}
	}
	printf("subsequence is: ");
	for(i = strind-1;i>=0;i--){
		printf("%c",str[i] );
	}
	printf("\n");
}

int find_max(int a,int b){
	if(a>b)
		return a;
	else
		return b;
}