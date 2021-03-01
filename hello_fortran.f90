subroutine hello_world() bind(c, name="c_hello_world")
  print *, "Fortran: Hello world!"
end subroutine

