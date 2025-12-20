class dog:
    species = "canis familiaris"
    
    def __init__(self, breed, age):
        self.breed = breed
        self.age = age
    
    def display_details(self):
        print("species: ", dog.species)
        print("breed: ", self.breed)
        print("age: ", self.age, "years")
        print("-------------------------")

dog1 = dog("Labrador retriver", 3)
dog2 = dog("German Shepherd", 5)

dog1.display_details()
dog2.display_details()