# Date 10/2/2022
# By: Vivek Kumar
# Find the GCD(greatest common divisor) of a number using recursion

def gcd(a, b):
    assert int(a) == a and int(b) == b, "a and b must be integers"
    if a < 0:
        a = -1*a
    if b < 0:
        b = -1*b
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print(gcd(15, 20))
