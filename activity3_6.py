height = float(input("enter your height in cm: "))
weight = float(input("enter your weight in kg: "))
BMI = weight/(height/100)**2
print("your BMI is ", BMI)
if BMI <=18.4:
    print("you are underweight")
elif BMI <= 24.9:
    print("you are healthy")
elif BMI <= 29.9:
    print("you are overweight")
elif BMI <= 34.9:
    print("your are severely overweight")
elif BMI <= 39.9:
    print("your are obese")
else:
    print("you are severely obese")