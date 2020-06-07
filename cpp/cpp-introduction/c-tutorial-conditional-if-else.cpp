#include <bits/stdc++.h>

using namespace std;



int main()
{
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');


    std::string dataSet[] = {
        "Greater than 9", "one", "two", "three", "four",
        "five", "six", "seven", "eight", "nine"};

    if (n > 9) {
        std::cout << dataSet[0];
    } else {
        std::cout << dataSet[n];
    }
    return 0;
}

