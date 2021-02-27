module number_test
  use iso_c_binding, only: c_int, c_double, c_double_complex
contains

subroutine num_addition(a, b, ans) bind(c, name="c_num_addition")
  integer(c_int), intent(in) :: a
  real(c_double), intent(in) :: b
  real(c_double), intent(out) :: ans

  ans = a + b
end subroutine

function cplxdiv(u ,v) bind(c, name="c_cplxdiv")
  complex(c_double_complex), intent(in) :: u, v
  complex(c_double_complex) :: cplxdiv

  cplxdiv = u / v
end function


end module
