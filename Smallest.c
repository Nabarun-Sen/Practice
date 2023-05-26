#include<stdio.h>
#include<string.h>
void main()
{
    float x,y,z;

    printf("Enter to check: ");
    scanf("%f%f%f", &x,&y,&z);

    if(x<y)
        if(x<z)
            printf("%f is the smallest",x);
        else
            printf("%f is the smallest",z);
    else if(y<z)
        if(y<x)
            printf("%f is the smallest",y);
        else
            printf("%f is the smallest",x);
    else
        printf("%f is the smallest",z);
}