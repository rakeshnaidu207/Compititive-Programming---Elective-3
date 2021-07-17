# Write the function getKthDigit(n, k) that takes 
# a possibly-negative int n and a non-negative int k, 
# and returns the kth digit of n, starting from 0, counting from the right.
# if the kth digit is not present return 0 



def fun_get_kth_digit(digit, k):
    l=[]
    count=0
    digit=abs(digit)
    while(digit>0):#495,1
        x=digit%10
        l.append(x)
        digit=digit//10
        count+=1
    if(k>len(l)-1):
        return 0
    return l[k]



