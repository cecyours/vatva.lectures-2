
#include<stdio.h>
/**
 * numbers : [0...9]
 * alphabet [a...z, A...Z]
 * special symbio [@,(,*,^,@,*,(,!,#,*&,(,*,&,$,!,(),),),),]
 * string ["kites","HelloWorld","welcome"]
 * 
 * ------------------- value : numberic
 * int : +ve, -ve, zero : natural number example : 0,  1, 3,4,5
 * float : all int + decimalc  example : 329.428, ....
 * double : all float, int example : more larger then float
 * 
 * ------------------ value : non-numerical  like Textual
 * char : single latter like 'a', 'b', '8', '-'
 * string : multiple character , in double quote, "kites..."
  */
int main()
{
    int i = 0; // %d
    float f = 821.45468; // %f
    double d = 821.45468; // %lf
    char ch = 'k'; //%c
    char name[] = "Never me";


    printf("      int  : %d\n",i);
    printf("    float  : %f\n",f);
    printf("   double  : %lf\n",d);
    printf("character  : %c\n",ch);
    printf("    String : %s\n",name);

    return 0;
}