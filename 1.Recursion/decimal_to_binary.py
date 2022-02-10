# Date 10/2/2022
# By: Vivek Kumar
# Convert a number from binary to decimal using recursion

def decimalToBinary(n):
    assert int(n) == n, "n must be a non-negative integer"
    if n == 0:
        return 0
    else:
        return n % 2 + 10*decimalToBinary(n//2)


print(decimalToBinary(5))
