class parrot:
    species = "bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age
blu = parrot("blu", 10)
woo = parrot("woo", 15)
print("blu is a {}".format(blu.species))
print("woo is also a {}",format(woo.species))
print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woo.name, woo.age))
