    .data
hello: .ascii "Hello from Assembly!"
hello_len = . - hello
    .text
    .globl hello_assembly
    .type hello_assembly, @function
hello_assembly:
    push %rbp
    mov %rsp, %rbp
    mov $1, %rax
    mov $1, %rdi
    lea .cursed_pie, %rsi
    mov $hello_len, %rdx
    syscall
    pop %rbp
    ret
