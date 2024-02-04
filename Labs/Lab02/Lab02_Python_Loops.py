
#Part 1
##Take the following list and multiply all list items together.
part1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
result1 = 1

for i in part1:
    result1 = result1 * i

print('The results for Part 1 are', result1)

#Part 2
##Take the following list and add all list items together.
part2 = [-1, 23, 483, 8573, -13847, -381569, 1652337, 718522177]
result2 = 0

for i in part2:
    result2 = result2 + i

print('The results for Part 2 are', result2)

#Part 3
##Take the following list and only add together those list items which are even. 
###You can use the following snippet of code to see if a number is even or odd. 
####The % operation is called Modulo and is used to find the remainder after division of one number by another. 
#####We divide by 2 and look at the remainder; if there is no remainder the number is even, if there is a remainder the number is odd.
part3 = [146, 875, 911, 83, 81, 439, 44, 5, 46, 76, 61, 68, 1, 14, 38, 26, 21] 
result3 = 0

for i in part3:
    if i % 2 == 0:
        result3 = result3 + i

print('The results for Part 3 are', result3)



#Bonus
##Part 1 using While Loop
##part4 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
##result4 = 1

##i = 0
##while i < len(part4):
    ##result4 = result4 * part4[i]
    ##i = i + 1