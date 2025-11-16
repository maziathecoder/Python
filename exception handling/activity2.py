try:
    num1,num2=eval(input("enter two numbers, seperated by a comma: "))
    result = num1 / num2
    print("the result is", result)
except ZeroDivisionError:
    print("divosion by zero is error")
except SyntaxError:
    print("comma is missing enter number seperated by comma like this 1,2")
except:
    print("wrong input")
else:
    print("no exceptions")
finally:
    print("this will execute no matter what")