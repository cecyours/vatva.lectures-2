#include<stdio.h>
void main(){

    float area, b, h;

    printf("Enter base : ");
    scanf("%f",&b);
    printf("Enter height : ");
    scanf("%f",&h);

    area = (b*h)*1/2;

    printf("your ans : %.2f\n",area);
}