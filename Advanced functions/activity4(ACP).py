#      PART 1
num = int(input("enter a number: "))
odd_numbers = [i for i in range(1, num) if i %2!=0]
even_numbers = [i for i in range(1, num) if i %2==0]
print(odd_numbers)
print(even_numbers)


#      PART 2
fruits = ['apple', 'banana', 'cherry', 'mango', 'orange']
cap_fruits = [fruit.capitalize() for fruit in fruits]
print("Original fruits list: ", fruits)
print("Capitalized fruits list: ", cap_fruits)