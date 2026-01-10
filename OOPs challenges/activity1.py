import random
class fruitquiz:
    def __init__(self):
        self.fruits = {'apple':'red','orange':'orange','watermelon':'green','banana':'yellow'}
    def quiz(self):
        while (True):
            fruit, color = random.choice(list(self.fruits.items()))
            print("what is the color of {}".format(fruit))
            user_answer = input()
            if (user_answer.lower() == color):
                print("correct answer")
            else:
                print("wrong answer")
            option = int(input("enter 0, if you want to play again otherwice enter 1: "))
            if (option):
                break
print("welcome to fruit Quiz")
fq = fruitquiz()
fq.quiz()