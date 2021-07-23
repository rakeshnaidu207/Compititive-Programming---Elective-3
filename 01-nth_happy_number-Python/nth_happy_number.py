# Write the function nth_happy_number(n) which takes a non-negative integer 
import nth_happy_number

# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:

# https://en.wikipedia.org/wiki/Happy_number#:~:text=In%20number%20theory%2C%20a%20happy,starting%20with%20and%20eventually%20reaches
# Read more about the happy number from the above link.

# assert(nth_happy_number(1) == 1)
# assert(nth_happy_number(2) == 7)
# assert(nth_happy_number(3) == 10)
# assert(nth_happy_number(4) == 13)
# assert(nth_happy_number(5) == 19)
# assert(nth_happy_number(6) == 23)
# assert(nth_happy_number(7) == 28)
# assert(nth_happy_number(8) == 31)



#helper function to find the squares of digits
def numSquareSum(n): 
    squareSum = 0; 
    while(n): 
        squareSum += (n % 10) * (n % 10); 
        n = int(n / 10); 
    return squareSum; 
  
#to find out if it is a happy number or not
def isHappynumber(n): 
    slow = n; 
    fast = n; 
    while(True): 
        slow = numSquareSum(slow); 
        fast = numSquareSum(numSquareSum(fast)); 
        if(slow != fast): 
            continue; 
        else: 
            break; 
    return (slow == 1); 
#finding nth happy primes

def nth_happy_number(n):
    found = 0
    guess = 0
    while (found <= n):
        guess += 1
        #print(guess)
        if (isHappynumber(guess)):
            found += 1
            #print(guess)
    return guess

