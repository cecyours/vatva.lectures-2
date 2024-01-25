#include<stdio.h>
int main()
{

    float marks;

    printf("Enter the marks : ");
    scanf("%f",&marks);


    printf("your marks : %f\n",marks);

    if(marks>33)
    {
        printf("welcome");
    }
    else{
        printf("bye bye..");
    }
    return 0;
}