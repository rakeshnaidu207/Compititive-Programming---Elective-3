# Python program to check if a number is a palindromic prime number or not

#Step 1: Taking the input from the user
num=int(input("Please enter the number: "))

# Reversing the number using slicing
reverse= int(str(num)[::-1])

# Checking number for palindrome and then for prime number
if num==reverse:
    if num>1:
        for i in  range(2,num):
            if num%i==0:
                print(num,"is not a prime number, but is a palindrome number!")
                break
        else:
            print("This is a prime as well as a palindrome number!")
else:
    if num>1:
        for i in  range(2,num):
            if num%i==0:
                print(num," This is not a prime nor a palindrome number.")
                break
        else:
            print("This is a prime number but not a palindrome number!")