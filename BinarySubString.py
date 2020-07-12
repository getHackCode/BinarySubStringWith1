##########
#EG:1 11111011101011->this is converted to the below line
#ANS  12345012301012->output->sum of all the integers in this string
##########
def numSub(s):
    res, currsum = 0,0
    for digit in s:
        if digit == '0':
            currsum = 0
        else:
            currsum += 1 
            res+=currsum 
    return res % (10**9+7)
n = input("Enter a string")
print("NUMBER OF SUBSTRING WITH ONLY 1s",numsub(n))
