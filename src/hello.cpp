#include <iostream>

extern "C" {
    #include "challenge.h"
}

using namespace std;

extern "C" void hello_cpp(int c) {
    cout << "Hello from C++!" << endl;
    challenge(c + 5);
}