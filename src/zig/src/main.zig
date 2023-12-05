const std = @import("std");
const challenge = @cImport(@cInclude("challenge.h")).challenge;

export fn hello_zig(c: c_int) callconv(.C) void {
    std.io.getStdOut().writer().print("Hello from Zig!\n", .{}) catch unreachable;

    _ = challenge(c + 5);
}
