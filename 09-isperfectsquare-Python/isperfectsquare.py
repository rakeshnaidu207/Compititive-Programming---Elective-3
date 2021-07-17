# isPerfectSquare(n) [10pts]
# Write the function isPerfectSquare(n) that takes a possibly-non-int value, and returns True if
# it is an int that is a perfect square (that is, if there exists an integer m such that
# m**2 == n), and False otherwise. Do not crash on non-ints nor on negative ints.

import math
def isperfectsquare(n):
    if(n>=0) and (n==(int((math.sqrt(n))* (math.sqrt(n))))):
        return True
    elif(type(n)==str or type(n)==float or n<0):
        return False
    