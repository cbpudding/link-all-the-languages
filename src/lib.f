subroutine hello_fortran() bind(C, name="hello_fortran")
	integer, dimension(3) :: current
	call idate(current)
	if (current(2) == 12) then
		write(*, '(a)') "Merry Christmas from Fortran!"
	else
		write(*, '(a)') "Hello from Fortran!"
	end if
end subroutine
