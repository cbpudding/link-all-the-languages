#include <ctime>
#include <iostream>

using namespace std;

extern "C" void hello_cpp() {
	time_t timestamp = time(NULL);
	struct tm *current = localtime(&timestamp);
	if(current->tm_mon == 11) {
		cout << "Merry Christmas from C++!" << endl;
	} else {
		cout << "Hello from C++!" << endl;
	}
}
