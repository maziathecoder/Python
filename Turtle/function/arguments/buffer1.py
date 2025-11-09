def emplyee(name):
    print(name)
def salary(exp):
    if exp >= 5:
        return 3000000
    elif exp >= 3:
        return 1000000
    else:
        return 5000000
emplyee("mazia")
a = salary(6)
print("the salary of emplyee is ", a)