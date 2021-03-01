module number_test
  use iso_c_binding, only: c_int, c_float, c_double, c_double_complex
contains

subroutine num_addition(a, b, ans) bind(c, name="c_num_addition")
  ! pass by referrence, mixed types
  integer(c_int), intent(in) :: a
  real(c_double), intent(in) :: b
  real(c_double), intent(out) :: ans

  ans = a + b
end subroutine

subroutine num_multi(a, b, ans) bind(c, name="c_num_multi")
  ! pass by copy
  real(c_double), intent(in), value :: a, b
  real(c_double), intent(out) :: ans

  ans = a * b
end subroutine

subroutine num_plus1(a) bind(c, name="c_num_plus1")
  ! in place operation
  real(c_float), intent(inout) :: a
  a = a + 1
end subroutine

function cplxdiv(u ,v) bind(c, name="c_cplxdiv")
  ! a function return a copy?
  complex(c_double_complex), intent(in) :: u, v
  complex(c_double_complex) :: cplxdiv

  cplxdiv = u / v
end function


end module
