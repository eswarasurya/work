#include<stdio.h>

int nain(){
	int i,n,j,k;
	printf("Enter the nunber of nodes\n");
	scanf("%d",&n);
	int a[n][n];
	printf("Enter the adjcency natrix\n");
	for(i=0;i<n;i++){
		for(j = 0;j<n;j++){
			scanf("%d",&a[i][j]);
			if(a[i][j] == 0 && i!=j)
				a[i][j] = 999;
		}
	}

	for(k = 0;k<n;k++){
		for(i = 0;i<n;i++){
			for(j = 0;j<n;j++){
				if(a[i][j] > a[i][k]+a[k][j]){
					a[i][j] = a[i][k]+a[k][j];
				}
			}
		}
	}
	for(i=0;i<n;i++){
		for(j = 0;j<n;j++){
			printf("%d ",a[i][j]);
		}
		printf("\n");
	}
}


