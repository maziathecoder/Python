def add(p,q):
    return p+q
def sub(p,q):
    return p-q
def divide(p,q):
    return p/q
def multiply(p,q):
    return p*q
print("please select the operation")
print("a. Add")
print("b. Sub")
print("c. Divide")
print("d. multiply")
choice = input("please enter your choice(a/ b/ c/ d/): ")
num1 = int(input("please enter your first number: "))
num2 = int(input("please enter your second number: "))
if choice=="a":
    print(num1, "+" ,num2, "=", add(num1,num2))
elif choice=="b":
    print(num1, "-" ,num2, "=", sub(num1,num2))
elif choice=="c":
    print(num1, "/" ,num2, "=", divide(num1,num2))
elif choice=="d":
    print(num1, "*" ,num2, "=", multiply(num1,num2))
else:
    print("this is an invalid input!")