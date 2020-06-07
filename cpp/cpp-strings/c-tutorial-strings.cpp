#include <iostream>
#include <string>
using namespace std;

int main() {
	std::string a, b;
    getline(std::cin, a);
    getline(std::cin, b);

    std::cout << a.size() << " " << b.size() << endl;
    std::cout << a + b << endl;
    char _a = a[0];
    a[0] = b[0];
    b[0] = _a;
    std::cout << a << " " << b ;
  
    return 0;
}


