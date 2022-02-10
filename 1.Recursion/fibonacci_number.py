# Date 10/2/2022
# By: Vivek Kumar
# Find the fibonacci of a number using recursion

def fibonacci(n):
    assert n >= 0 and int(n) == n, "n must be a non-negative integer"
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
