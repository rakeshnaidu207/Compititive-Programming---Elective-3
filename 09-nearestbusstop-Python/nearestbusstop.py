# Write the function nearestBusStop(street) that takes a 
# non-negative int street number, and returns the nearest 
# bus stop to the given street, where buses stop every 8th street, 
# including street 0, and ties go to the lower street, 
# so the nearest bus stop to 12th street is 8th street, 
# and the nearest bus stop to 13 street is 16th street.



def fun_nearestbusstop(street):
    busstop=0
    if(street%8<=4):
        s=int(street/8)
        r=s*8
        return r
    elif(street%8>=4):
        i=int(street/8)
        t=(i+1)*8
        return t
   