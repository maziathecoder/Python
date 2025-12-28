class reverse:
    def __init__(self, s=""):
        self.s = s
    def  reverse_string(self):
        return self.s[::-1]
word = input("enter a word: ")
obj = reverse(word)
print("reversed string: ", obj.reverse_string())