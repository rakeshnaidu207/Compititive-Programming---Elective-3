# Write the function nearestBusStop(street) that takes a 
# non-negative int street number, and returns the nearest 
# bus stop to the given street, where buses stop every 8th street, 
# including street 0, and ties go to the lower street, 
# so the nearest bus stop to 12th street is 8th street, 
# and the nearest bus stop to 13 street is 16th street.



def fun_nearestbusstop(street):
    a=street%8
    if(a<=4):
        s=street/8
        u=int(s)
        r=u*8
        return r
    elif(a>=4):
        i=street/8
        g=int(i)
        t=(g+1)*8
        return t
   