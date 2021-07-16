# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(x):
    x=abs(x)
    prev_digit= -1
    while (x > 0):
        one_digit = x%10
        x //=10
        if (prev_digit == one_digit):
            return True
        prev_digit=one_digit
    return False