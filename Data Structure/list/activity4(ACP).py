start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
squares = []
for num in range(start, end + 1):
    squares.append(num * num)
even_squares = []
odd_squares = []
for value in squares:
    if value % 2 == 0:
        even_squares.append(value)
    else:
        odd_squares.append(value)
print("\nSquare values:", squares)
print("Even squares:", even_squares)
print("Odd squares:", odd_squares)