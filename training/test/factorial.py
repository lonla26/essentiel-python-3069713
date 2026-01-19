def factorial(n):
  """
  Compute the factorial of n.

  """
  if n < 0 :
    raise ValueError("Received negative input")
  result = 1
  for i in range(1,n+1):
    result *= i
  return result