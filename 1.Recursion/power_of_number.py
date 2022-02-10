# Date 10/2/2022
# By: Vivek Kumar
# Find the power of a number using recursion

def power(base, exp):
    assert exp >= 0 and int(exp) == exp, "exp must be a non-negative integer"
    if exp == 0:
        return 1
    if exp == 1:
        return base
    return base*power(base, exp-1)


print(power(-2, 5))
