# Without using iteration and without using strings, 
# write the recursive function onlyEvenDigits(L), 
# that takes a list L of non-negative integers 
# (you may assume that), and returns a new list of 
# the same numbers only without their odd digits 
# (if that leaves no digits, then replace the number with 0). 
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844]. 
# Also the function returns the empty list if the original list is empty. 
# Remember to not use strings. You may not use loops/iteration in this problem.

gv=0
s=[]
def remOdds(v):
	global gv
	if(v>0):
		ld=v%10
		remOdds(v//10)
		if(ld%2==0):
			gv=gv*10+ld


def fun_recursion_onlyevendigits(l):
	if l==[]:
		return l
	global gv
	if(len(l)!=0):
		gv=0
		remOdds(l[0])
		s.append(gv)
		fun_recursion_onlyevendigits(l[1:])
	return s
	# your code goes here

#print(fun_recursion_onlyevendigits(readList()))

