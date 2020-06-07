#include <stdio.h>

int max_of_four(int a, int b, int c, int d){
    int min=a;
    if(min<=b) 
        min=b;
    if(min<=c) 
        min=c;
    if(min<=d) 
        min=d;
    return min;        
}

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}

