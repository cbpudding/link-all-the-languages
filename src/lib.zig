const std = @import("std");

export fn hello_zig() void {
    const stdout = &std.io.getStdOut().outStream().stream;
    if (stdout.print("Hello from Zig!\n", .{})) |_| {} else |err| {
        std.debug.warn("{}", .{err});
    }
}
