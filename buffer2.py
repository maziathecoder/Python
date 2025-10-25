str1 = input("please enter a sentence: ")
total = 1
for i in range(len(str1)):
    if(str1[i]==" "):
        total = total + 1
print("total number of words in this string: ",total)