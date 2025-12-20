class Dog:
    # Class variable (shared by all objects)
    species = "Canis familiaris"

    # Constructor with two instance variables
    def __init__(self, breed, age):
        self.breed = breed      # Instance variable
        self.age = age          # Instance variable

    # Method to display dog details
    def display_details(self):
        print("Species:", Dog.species)
        print("Breed:", self.breed)
        print("Age:", self.age, "years")
        print("------------------------")


# Creating two different Dog objects (different breeds)
dog1 = Dog("Labrador Retriever", 3)
dog2 = Dog("German Shepherd", 5)

# Displaying their details
dog1.display_details()
dog2.display_details()
