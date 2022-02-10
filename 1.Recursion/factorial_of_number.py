# Date 10/2/2022
# By: Vivek Kumar
# Find the factorial of a number using recursion

def factorial(n):
    assert n >= 0 and int(n) == n, "n must be a non-negative integer"
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(100))
