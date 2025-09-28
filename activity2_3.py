name = "penguin"
age = 50
is_student = True
weight = 38.5
print("name : ", name)
print("datatype of name is ", type(name))
print("age : ", age)
print("datatype of age is ", type(age))
print("is_student : ", is_student)
print("datatype of is_student is ", type(is_student))
print("weight : ", weight)
print("datatype of weight is ", type(weight))

print("\nafter typecasting...")
age = str(age)
print(age)
print("datatype of age is ", type(age))
weight = int(weight)
print(weight)
print("datatype of weight is ", type(weight))