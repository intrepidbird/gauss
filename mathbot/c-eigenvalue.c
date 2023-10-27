#include<stdio.h>
#include<conio.h>
#include<math.h>

#define SIZE 10

int main()
{
	 float a[SIZE][SIZE], x[SIZE],x_new[SIZE];
	 float temp, lambda_new, lambda_old, error;
	 int i,j,n, step=1;
	 clrscr();
	 /* Inputs */
	 printf("Enter Order of Matrix: ");
	 scanf("%d", &n);
	 printf("Enter Tolerable Error: ");
	 scanf("%f", &error);
	 /* Reading Matrix */
	 printf("Enter Coefficient of Matrix:\n");
	 for(i=1;i<=n;i++)
	 {
		  for(j=1;j<=n;j++)
		  {
			   printf("a[%d][%d]=",i,j);
			   scanf("%f", &a[i][j]);
		  }
	 }
	 /* Reading Intial Guess Vector */
	 printf("Enter Initial Guess Vector:\n");
	 for(i=1;i<=n;i++)
	 {
		  printf("x[%d]=",i);
		  scanf("%f", &x[i]);
	 }
	 /* Initializing Lambda_Old */
	 lambda_old = 1;
	 /* Multiplication */
	 up:
	 for(i=1;i<=n;i++)
	 {
		  temp = 0.0;
		  for(j=1;j<=n;j++)
		  {
		   	temp = temp + a[i][j]*x[j];
		  }
		  x_new[i] = temp;
	 }
	 /* Replacing */
	 for(i=1;i<=n;i++)
	 {
	  	x[i] = x_new[i];
	 }
	 /* Finding Largest */
	 lambda_new = fabs(x[1]);
	 for(i=2;i<=n;i++)
	 {
		  if(fabs(x[i])>lambda_new)
		  {
		   	lambda_new = fabs(x[i]);
		  }
	 }
	 /* Normalization */
	 for(i=1;i<=n;i++)
	 {
	  	x[i] = x[i]/lambda_new;
	 }
	 /* Display */
	 printf("\n\nSTEP-%d:\n", step);
	 printf("Eigen Value = %f\n", lambda_new);
	 printf("Eigen Vector:\n");
	 for(i=1;i<=n;i++)
	 {
	  	printf("%f\t", x[i]);
	 }
	 /* Checking Accuracy */
	 if(fabs(lambda_new-lambda_old)>error)
	 {
		  lambda_old=lambda_new;
		  step++;
		  goto up;
	 }
	 getch();
	 return(0);
}
