#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n,i;
    std::cin >> n;

    int arr[n];

    for(i=0;i<n;i++){
        std::cin >> arr[i];
    }

    for(i=n-1;i>=0;i--){
        std::cout << arr[i] <<" ";
    }
    return 0;
}

