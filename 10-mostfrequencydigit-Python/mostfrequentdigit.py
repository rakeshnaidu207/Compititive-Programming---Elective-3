# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
     p = abs(n)
     if p == 0:
        return 0
     else:
        while(p>0):
            num=p
            p1 = num%10
            num = num//10
            p2= num%10
            if(p1 != p2 and p>9):
                p=p//10
            else:
                return p1
        return min(p1,p2)
	