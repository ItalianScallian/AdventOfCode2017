import math

#returns the distance from the center of a spiral matrix
#where the bottom left corner is an odd square
#only works when the number given is on the bottom row
def Distance(Num):
    multiplier = []
    my_list = []
    for i in range(1, int(math.sqrt(Num))+1, 2):
        if (i*i) < Num:
            my_list.append(i*i)
            multiplier.append(i)
    multiplier.append(multiplier[-1]+2)
    large_square = multiplier[-1]*multiplier[-1]
    difference = large_square - Num
    if difference > int(math.sqrt(large_square)):
        distance = abs(multiplier[-1]-difference-1)
    else:
        distance = multiplier[-1]-difference-1
    return distance
    

if __name__== "__main__":
    print Distance(225)

        
