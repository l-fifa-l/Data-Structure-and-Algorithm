# Date 10/2/2022
# By: Vivek Kumar
# Find the sum of digits of a number using recursion

def sumOfDigits(n):
    assert n >= 0 and int(n) == n, "n must be a non-negative integer"
    if n == 0:
        return 0
    else:
        return n % 10 + sumOfDigits(n // 10)
