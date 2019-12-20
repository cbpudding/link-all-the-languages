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
    return sh("{} -Os -march=native -mtune=native {}".format(env('CC', "gcc"),
                             args))
def CXX(args):
    return sh("{} -Os -march=native {} -mtune=native ".format(env('CXX', "g++"),
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
    return sh("{} -Os -march=native -mtune=native {}".format(env('FORTRAN', "gfortran"),
                             args))
def D(args):
    return sh("{} -O -release {}".format(env('DLANG', 'dmd'),
                             args))

#### Targets Section ####

@output("target/main.o")
@dependent("src/main.c")
def main_o(**info):
    return seq_join(CC("-o target/main.o -c src/main.c"))

@output("target/release/libhello_c.a")
@dependent("src/lib.c")
def c_a(**info):
    return seq_join(CC("-c src/lib.c -o target/release/libhello_c.o"),
                AR("rcs target/release/libhello_c.a target/release/libhello_c.o"))

@output("target/release/libhello_cpp.a")
@dependent("src/lib.cpp")
def cpp_a(**info):
    return seq_join(CXX("-c src/lib.cpp -o target/release/libhello_cpp.o"),
                AR("rcs target/release/libhello_cpp.a target/release/libhello_cpp.o"))

@output("target/release/libhello_carp.a")
@dependent("src/lib.carp")
def carp_a(**info):
    return seq_join(sh("carp -b --generate-only src/lib.carp"),
                    CC("-I $CARP_DIR/core -c out/main.c -o target/release/libhello_carp.o"),
                    sh("rm -r out"),
                    AR("rcs target/release/libhello_carp.a target/release/libhello_carp.o"))

@output("target/release/libhello_d.a")
@dependent("src/lib.d")
def d_a(**info):
    return seq_join(D("-c src/lib.d -oftarget/release/libhello_d.o"),
                    AR("rcs target/release/libhello_d.a target/release/libhello_d.o"))

@output("target/release/libhello_fortran.a")
@dependent("src/lib.f95")
def fortran_a(**info):
    return seq_join(FORTRAN("-ffree-form -c src/lib.f95 -o target/release/libhello_fortran.o"),
                AR("rcs target/release/libhello_fortran.a target/release/libhello_fortran.o"))

@output("target/release/libhello_nim.a")
@dependent("src/lib.nim")
def nim_a(**info):
    return seq_join(sh("nim compile --noMain --app:staticlib -o:libhello_nim.a src/lib.nim"),
                    sh("mv libhello_nim.a target/release/libhello_nim.a"))

@output("target/release/libhello_rust.a")
@dependent(["src/lib.rs", "Cargo.toml", "Cargo.lock"])
def rust_a(**info):
    return seq_join(sh("cargo build --release --target-dir target"))

@output("target/release/libhello_zig.a")
@dependent("src/lib.zig")
def zig_a(**info):
    return seq_join(ZIG("build-lib src/lib.zig --output-dir target/release --name hello_zig -fPIC --bundle-compiler-rt"))

def funcs_header_from_names(func_names):
    externs = "\n".join("extern const void {}();".format(name) for name in func_names)
    externs += "\n\n"
    externs += "const void (*hello[])() = {{ {} }};".format(", ".join(func_names))
    externs += "\n"
    externs += "#define NUMBER_OF_LANGUAGES sizeof(hello) / sizeof(hello[0])"
    externs += "\n"
    return externs

def funcs_header_from_funcs(funcs):
    names = {
	c_a: 'hello_c',
        cpp_a: 'hello_cpp',
        carp_a: 'hello_carp',
        d_a: 'hello_d',
        fortran_a: 'hello_fortran',
        nim_a: 'hello_nim',
        rust_a: 'hello_rust',
        zig_a: 'hello_zig'
    }
    return funcs_header_from_names([names[x] for x in funcs])

def linker_flags_from_funcs(funcs):
    flags = {
        cpp_a: '-lstdc++',
        carp_a: '-lm',
        d_a: '-lphobos2',
        fortran_a: '-lgfortran'
    }
    flaglist = []
    for f in funcs:
        if f in flags:
            flaglist.append(f)
    return " ".join(flags[x] for x in flaglist)

def write_funcs_header_with_funcs(funcs):
    data = funcs_header_from_funcs(funcs)
    with open("src/functions.h", "w") as funcsfile:
        funcsfile.write(data)

@output("target/link-all-languages")
@partial_dependent([c_a, cpp_a, carp_a, d_a, fortran_a, nim_a, rust_a, zig_a])
@dependent(main_o)
def link_all_the_languages(output, deps, partial_deps):
    deps = par_join(*[f() for f in partial_deps])
    target = lambda use_deps, flags: CC("-o target/link-all-languages target/main.o {} -Wl,--gc-sections -lpthread -ldl -fuse-ld=lld {}".format(" ".join(x.out for x in use_deps), flags))
    def linked():
        statuses = deps()
        use_funcs = [x[1] for x in filter(lambda x: x[0], zip(statuses, partial_deps))]
        write_funcs_header_with_funcs(use_funcs)
        main_o()()
        return target(use_funcs, linker_flags_from_funcs(use_funcs))()
    return linked

#### Build Invocation ####

job = seq_join(sh("mkdir -p target/release"),
               link_all_the_languages())
job()
