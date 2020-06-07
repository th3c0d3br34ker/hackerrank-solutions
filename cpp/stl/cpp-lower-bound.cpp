#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int size, a;
    cin >> size;
    vector <int> arr;

    for(int i = 0; i < size; i ++) {
        cin >> a;
        arr.push_back(a);
    }

    int q;
    cin >> q;

    for(int i = 0; i < q; i ++) {
        int n;
        cin >> n;
        vector<int> :: iterator low = lower_bound(arr.begin(), arr.end(), n);
        if (arr[low - arr.begin()] == n)
            cout << "Yes" << " " << low - arr.begin() + 1 << endl;
        else 
            cout << "No" << " " << low - arr.begin() + 1 << endl;
    }   
    return 0;
}

