#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{   
    int a,b;
    float x,y;
    scanf("%d %d",&a,&b);
    scanf("%f %f",&x,&y);


    printf("%d %d\n%0.1f %0.1f",(a+b),(a-b),(x+y),(x-y));
    return 0;
}


