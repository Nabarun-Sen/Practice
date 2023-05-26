#include<stdio.h>
void main()
{
int n;
printf("Enter a number: ");
scanf("%f",&n);
(n>0) ? printf("Positive"):
(n<0) ? printf("Negative"): 
printf("Zero");
}