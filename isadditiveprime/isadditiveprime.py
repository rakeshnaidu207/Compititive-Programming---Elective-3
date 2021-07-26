
 
# Check if N is prime or not
def isPrime(n):
 
    # Corner Cases
    if (n <= 1):
        return False
 
    if (n <= 3):
        return True
 
    # This is checked to skip
    # middle five numbers
    if (n % 2 == 0 or n % 3 == 0):
        return False
         
    i = 5
    while(i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6
 
    return True
 
# Function to get sum of digits
def getSum(n):
 
    sum = 0
    while (n != 0):
        sum = sum + n % 10
        n = n / 10
 
    # Return the sum of digits
    return sum
 
# Function to check whether
# the given number is
# Additive Prime number or not
def isAdditivePrime(n):
 
    # If number is not prime
    if (not isPrime(n)):
        return False
 
    # Check if sum of digits
    # is prime or not
    return isPrime(getSum(n))
 
# Driver Code
 
# Given Number N
N = 23
 
# Function Call
if (isAdditivePrime(N)):
    print ("Yes")
else:
    print ("No")