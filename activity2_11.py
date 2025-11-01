rows = int(input("enter the number of rows: "))
number = 1
print("floyds triangle")
for i in range (1,rows + 1):
    for j in range (1,i +1):
        print(number, end=" ")
        number = number + 1
    print()