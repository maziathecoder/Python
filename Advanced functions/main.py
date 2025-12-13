# ---------- Part 1: Odd and Even Numbers ----------

# Take a number from the user
num = int(input("Enter a number: "))

# List of odd numbers under the input value
odd_numbers = [i for i in range(1, num) if i % 2 != 0]

# List of even numbers under the input value
even_numbers = [i for i in range(1, num) if i % 2 == 0]

print("Odd numbers:", odd_numbers)
print("Even numbers:", even_numbers)


# ---------- Part 2: Capitalize First Letter of Fruits ----------

# Create a list of fruits
fruits = ["apple", "banana", "cherry", "mango", "orange"]

# Convert first letter of each fruit to capital
capitalized_fruits = [fruit.capitalize() for fruit in fruits]

print("Original fruits list:", fruits)
print("Capitalized fruits list:", capitalized_fruits)
