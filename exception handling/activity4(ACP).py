try:
    age = int(input("Enter your age: "))
    if age <= 0 or age > 150:
        print("Invalid age. Please enter a realistic value.")
    else:
        print("Age is valid.")
        if age % 2 == 0:
            print("The age is even.")
        else:
            print("The age is odd.")
except ValueError:
    print("Error: Age must be a number.")