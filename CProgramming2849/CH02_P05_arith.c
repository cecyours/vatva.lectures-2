
//  5+4
#include <stdio.h>
int main()
{   

    int a,b,ans;
    char ch;

    printf("Enter expression : ");
    scanf("%d%c%d",&a,&ch,&b);

    if(ch=='+')
    {
        ans = a+b;
    }
    if(ch=='-')
    {
        ans = a-b;
    }

    /* 
        -, + , * , / 
     */
    printf("%d %c %d = %d\n",a,ch,b,ans);

    return 0;
}