#include <iostream>

using namespace std;

extern "C" void hello_cpp() {
    cout << "Hello from C++!" << endl;
}
