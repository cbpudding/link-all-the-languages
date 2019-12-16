import std.datetime;
import std.stdio;

extern(C) void hello_d() {
	auto current = cast(DateTime)Clock.currTime();
	if(current.month == Month.dec) {
		writeln("Merry Christmas from D!");
	} else {
		writeln("Hello from D!");
	}
}
