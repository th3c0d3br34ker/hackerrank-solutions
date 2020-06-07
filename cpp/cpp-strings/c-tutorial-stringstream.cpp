#include <sstream>
#include <vector>
#include <iostream>
using namespace std;

vector<int> parseInts(string str) {
	std::vector<int> number;
    std::stringstream ss(str);
    int num;
    while(ss >> num) {
        number.push_back(num);
        if (ss.peek() == ',')
            ss.ignore();
    }
    return number;
}

int main() {
    string str;
    cin >> str;
    vector<int> integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }
    
    return 0;
}


