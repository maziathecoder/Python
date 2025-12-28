class Reverse:
    def __init__(self, s=""):
        self.s = s

    def reverse_string(self):
        return self.s[::-1]


# taking input from the user
word = input("Enter a word: ")

# creating object of the class
obj = Reverse(word)

# printing the reversed string
print("Reversed string:", obj.reverse_string())
