rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    spaces = " " * (rows - i)
    stars = "*" * i
    print(spaces + stars + "  " + stars)