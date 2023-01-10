import std.stdio;

extern (C) bool challenge(int c);

extern (C) void hello_d(int c) {
    writeln("Hello from D!");
    challenge(c + 5);
}