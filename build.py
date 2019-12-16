#!/usr/bin/env python3
from os.path import getmtime as mod_time
from os import system, environ
from shutil import copy

# If a full dep fails, the task has failed. So, exit.
# If a partial dep fails, the task may handle it. So, pass a marker to the task.
# If a task has no deps, it is PHONY. Execute it if on active graph edge.

# Function attributes `deps`, `partial_deps`, and `out` are reserved.
# Additionally, the decorators that follow pass the keyword arguments
#  - `deps`
#  - `partial_deps`
#  - `output`
# to the decorated functions.

# Provide for annotation of task's dependencies
def dependent(deps):
    def dependent_1(func):
        def dep_func(*a, **b):
            b['deps'] = deps
            return func(*a, **b)
        dep_func.deps = deps
        if hasattr(func, 'partial_deps'):
            dep_func.partial_deps = func.partial_deps
        if hasattr(func, 'out'):
            dep_func.out = func.out
        return dep_func
    return dependent_1

# Dependencies that a task can finish without, but should update for
def partial_dependent(deps):
    def partial_dependent_1(func):
        def partial_dep_func(*a, **b):
            b['partial_deps'] = deps
            return func(*a, **b)
        partial_dep_func.partial_deps = deps
        if hasattr(func, 'deps'):
            partial_dep_func.deps = func.deps
        if hasattr(func, 'out'):
            partial_dep_func.out = func.out
        return partial_dep_func
    return partial_dependent_1

# Information about output
# Note that this is for convenience only, and is not used in the build graph
# This will pass a keyword argument `output` to the decorated function.
# This will also set an attribute `out` on the decorated function.
def output(out):
    def output_1(func):
        def output_func(*a, **b):
            b['output'] = out
            return func(*a, **b)
        output_func.out = out
        # Preserve wrapped function's special attributes
        if hasattr(func, 'deps'):
            output_func.deps = func.deps
        if hasattr(func, 'partial_deps'):
            output_func.partial_deps = func.partial_deps
        return output_func
    return output_1

# Composable join of delayed evaluation commands
# Guarantees evaluation order
# TODO: Preserve deps
# TODO: Decide what to execute based on deps
def seq_join(*arg):
    def seq_joined():
        for a in arg:
            result = a()
            if isinstance(result, int):
                if result != 0:
                    return False
            else:
                if not result:
                    return False
        return True
    return seq_joined

# Composable join of delayed evaluation commands
# Does not guarantee evaluation order
# Does guarantee exit status list order
# TODO: Preserve deps
# TODO: Decide what to execute based on deps
def par_join(*arg):
    def par_joined():
        return [a() for a in arg]
    return par_joined

# Delayed evaluation shell command
def sh(cmd):
    def command():
        print(cmd)
        return system(cmd)
    return command

# Pull variable from environment, with known default
def env(name, default):
    if name in environ.keys():
        return environ[name]
    else:
        return default

# Environment dependent build commands
def CC(args):
    return sh("{} {}".format(env('CC', "gcc"),
                             args))
def CXX(args):
    return sh("{} {}".format(env('CXX', "g++"),
                             args))
def AR(args):
    return sh("{} {}".format(env('AR', "ar"),
                             args))
def LD(args):
    return sh("{} {}".format(env('LD', "ld"),
                             args))
def ZIG(args):
    return sh("{} {}".format(env('ZIG', "zig"),
                             args))
def FORTRAN(args):
    return sh("{} {}".format(env('FORTRAN', "gfortran"),
                             args))

#### Targets Section ####

@output("target/debug/libhello_rust.a")
@dependent(["src/lib.rs", "Cargo.toml", "Cargo.lock"])
def rust_a(**info):
    return seq_join(sh("cargo build --target-dir target"))

@output("target/debug/libhello_cpp.a")
@dependent("src/lib.cpp")
def cpp_a(**info):
    return seq_join(CXX("-c src/lib.cpp -o target/debug/libhello_cpp.o"),
                AR("rcs target/debug/libhello_cpp.a target/debug/libhello_cpp.o"))

@output("target/debug/libhello_c.a")
@dependent("src/lib.c")
def c_a(**info):
    return seq_join(CC("-c src/lib.c -o target/debug/libhello_c.o"),
                AR("rcs target/debug/libhello_c.a target/debug/libhello_c.o"))

@output("target/debug/libhello_zig.a")
@dependent("src/lib.zig")
def zig_a(**info):
    return seq_join(ZIG("build-lib src/lib.zig --output-dir target/debug --name hello_zig -fPIC --bundle-compiler-rt"))

@output("target/debug/libhello_fortran.a")
@dependent("src/lib.f95")
def fortran_a(**info):
    return seq_join(FORTRAN("-ffree-form -c src/lib.f95 -o target/debug/libhello_fortran.o"),
                AR("rcs target/debug/libhello_fortran.a target/debug/libhello_fortran.o"))

@output("target/main.o")
@dependent("src/main.c")
def main_o(**info):
    return seq_join(CC("-o target/main.o -c src/main.c"))


def funcs_header_from_names(func_names):
    externs = "\n".join("extern const void {};".format(name) for name in func_names)
    externs += "\n"
    externs += "const void (*hello[])() = {{ {} }};".format(", ".join(func_names))
    externs += "\n"
    externs += "#define NUMBER_OF_LANGUAGES sizeof(hello) / sizeof(hello[0])"
    externs += "\n"
    return externs

@output("target/link-all-languages")
@partial_dependent([rust_a, cpp_a, c_a, zig_a, fortran_a])
@dependent(main_o)
def link_all_the_languages(output, deps, partial_deps):
    deps = par_join(rust_a(), cpp_a(), c_a(),
                zig_a(), fortran_a(), main_o())
    target = CC("-o target/link-all-languages target/main.o target/debug/libhello_rust.a target/debug/libhello_cpp.a target/debug/libhello_c.a target/debug/libhello_zig.a target/debug/libhello_fortran.a -Wl,--gc-sections -lpthread -ldl -fuse-ld=lld -lgfortran -lstdc++")
    def linked():
        deps()
        return target()
    return linked

#### Build Invocation ####

job = seq_join(sh("mkdir -p target/debug"),
               link_all_the_languages())
job()



@dependent("Hello!")
def heck():
    return 10

@output("target/link-all-languages")
@partial_dependent([rust_a, cpp_a, c_a, zig_a, fortran_a])
@dependent(main_o)
def link_all_the_languages(deps, partial_deps, output):
    return CC("-o target/link-all-languages {} -Wl,--gc-sections -lpthread -ldl -fuse-ld=lld -lgfortran -lstdc++".format(" ".join(x.out for x in deps + partial_deps)))
