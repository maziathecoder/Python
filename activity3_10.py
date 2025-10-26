num = int(input("enter the number: "))
p = num
numLen = 0
while p > 0:
    numLen = numLen + 1
    p = int(p / 10)
if numLen >= 4:
    numLen = int(numLen / 2)
    chk = 0
    while num > 0:
        rem = num % 10
        if chk == numLen:
            mid1 = rem
        elif chk == (numLen - 1):
            mid2  = rem
        num = int(num / 10)
        chk = chk + 1
    prod = mid1 * mid2
    print("\nproduct of mid digits (" +str(mid1)+ "*" +str(mid2)+ ")= ",prod)
else:
    print("please enter 4 digit or greater than 4 digit number")