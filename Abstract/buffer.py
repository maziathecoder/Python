class cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f"Iam a cat. My name is {self.name}. I am {self.age} years old.")
    def make_sound(self):
        print("meow")

class dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f"Iam a dog. My name is {self.name}. I am {self.age}years old.")
    def make_sound(self):
        print("bark")
cat1 = cat("Kitty", 2.5)
dog1 = dog("fluffy", 4)
for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()