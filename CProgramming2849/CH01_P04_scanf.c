#include<stdio.h>
void main(){

    int a,b,c;

    printf("enter value for a : ");
    scanf("%d",&a);

    printf("enter value for b : ");
    scanf("%d",&b);


    printf("-----------\n");
    printf("a : %d , b : %d\n",a,b);

    c = a+b;
    printf("%d + %d = %d\n",a,b,c);

}