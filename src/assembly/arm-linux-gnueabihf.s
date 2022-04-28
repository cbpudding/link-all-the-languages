    .data
hello: .ascii "Hello from Assembly!\n"
hello_len = . - hello
    .text
    .globl hello_assembly
    .type hello_assembly, %function
hello_assembly:
    mov r7, #4
    mov r0, #1
    ldr r1, =hello
    mov r2, #hello_len
    swi #0
    bx lr