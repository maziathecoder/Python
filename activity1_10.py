string = input("enter a word: ")
char = input("neter a character: ")
i = 0
count = 0
while i<len(string):
    if string[i]==char:
        count = count + 1
    i = i + 1
print("the occurance of the character: ", count)