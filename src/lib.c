#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void hello_c() {
	time_t timestamp = time(NULL);
	struct tm *current = localtime(&timestamp);
	if(current->tm_mon == 11) {
		puts("Happy Holidays from C!");
	} else {
		puts("Hello from C!");
	}
}
