proc challenge(c: cint): cint {.importc.}

proc hello_nim(c: cint) {.exportc.} =
    echo "Hello from Nim!"
    discard challenge(c + 5)