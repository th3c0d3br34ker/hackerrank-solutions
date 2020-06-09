#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int next_permutation(int n, char **s)
{

    int k, l;
    // 1. find the largest index k such that s[k] < s[k+1]
    for (k = n - 2; k >= 0; k--)
    {
        if (strcmp(s[k], s[k + 1]) < 0)
            break;
    }
    if (k < 0)
        return 0;

    // 2. find the largest index l greater than k such that s[k] < s[l]
    for (l = n - 1; l > k; l--)
    {
        if (strcmp(s[k], s[l]) < 0)
            break;
    }

    // 3. swap elements present at k, l
    char *tmp = s[k];
    s[k] = s[l];
    s[l] = tmp;

    // 4. reverse the sequence of elements from k+1 to n
    for (int i = k + 1, j = n - 1; i < j; i++, j--)
    {
        tmp = s[i];
        s[i] = s[j];
        s[j] = tmp;
    }
    return 1;
}


