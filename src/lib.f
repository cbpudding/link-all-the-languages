subroutine hello_fortran() bind(C, name="hello_fortran")
  write(*,'(a)') "Hello from Fortran!"
end subroutine
