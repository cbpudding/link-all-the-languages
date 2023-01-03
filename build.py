#!/usr/bin/python
# Build script for link-all-the-languages created by Alexander Hill(Breadpudding)

import os
import yaml

build = yaml.safe_load(open("build.yml", "r"))

# Utility function for finding executables in the PATH
def which(program):
    def is_exe(path):
        return os.path.isfile(path) and os.access(path, os.X_OK)

    path, _ = os.path.split(program)

    if path:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            victim = os.path.join(path, program)
            if is_exe(victim):
                return victim
    
    return None

def check_requirements(reqs, incs):
    for r in reqs.split():
        if which(r) == None:
            return False
    for i in incs.split():
        if False: # TODO: Check the library search path for the header files
            return False
    return True

# Step 1: Figure out what we can and can't compile on this system

entry_points = []
commands = []
libraries = set()
objects = []
runtimes = set()

# TODO: Check to see which runtimes we have available and check their
#       requirements. If the requirements are met add it to the set
#       so languages can be filtered based on what we have available. ~Alex

for lang, instr in build["languages"].items():
    # TODO: Ignore the language if the runtime required isn't listed above
    if check_requirements(instr["requires"], instr["includes"]):
        commands.append((instr["root"], instr["build"]))
        entry_points.append(instr["entry"])
        for lib in instr["library"].split():
            libraries.add(lib)
        objects.append(instr["output"])

# Step 2: Compile the entry point for the program itself

header = open("src/langs.h", "w")

for entry in entry_points:
    header.write("extern const void " + entry + "();" + os.linesep)

header.write(os.linesep + "const void (*ENTRY_POINTS[])() = {" + ", ".join(entry_points) + "};" + os.linesep)

header.close()

# Step 3: Build all the parts we can compile

base = os.getcwd()

for (root, cmds) in commands:
    os.chdir(base + root)
    for cmd in cmds:
        print(cmd)
        if os.system(cmd) != 0:
            exit(1)

# Step 4: Wrap everything up as one executable

os.chdir(base + "/src")

print("cc -c -o main.o main.c")
if os.system("cc -c -o main.o main.c") != 0:
    print("Failed to compile the program's entry point! Do you have a C compiler installed?")
    exit(1)

ld = "cc -o ../hello " + " ".join(["-l" + lib for lib in libraries]) + " main.o " + " ".join(objects)

print(ld)
if os.system(ld) != 0:
    print("Failed to link the program! Are we missing a dependency?")
    exit(1)