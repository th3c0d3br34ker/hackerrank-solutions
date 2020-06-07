#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n, i, t;
    cin >> n;
    vector<int> arr;
    for(i=0;i<n;i++){
        cin>> t;
        arr.push_back(t);
    }

    sort(arr.begin(),arr.end());
    
    for(i=0;i<n;i++){
        cout << arr[i] << " ";
    }
    return 0;
}

