    .data
hello: .ascii "Hello from Assembly!\n"
hello_len = . - hello
    .text
    .globl challenge
    .globl hello_assembly
    .type hello_assembly, @function
hello_assembly:
    /* Create a new call frame */
    push %rbp
    mov %rsp, %rbp
    /* Complete the challenge */
    mov %edi, %eax
    add $5, %eax
    mov %eax, %edi
    call challenge
    /* Print our message from Assembly */
    mov $1, %rax
    mov $1, %rdi
    lea hello(%rip), %rsi
    mov $hello_len, %rdx
    syscall
    /* Restore the old call frame and return */
    mov %rbp, %rsp
    pop %rbp
    ret
