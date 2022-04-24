subroutine hello_fortran () bind (C, name="hello_fortran")
    print *, "Hello from Fortran!"
end subroutine hello_fortran