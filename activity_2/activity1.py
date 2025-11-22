import random
playing = True
number = str(random.randint(10,20))
print("i will generat a number from 1 to 9, and we have to guess the number one digit at a time.")
print("the ends when you get one")
while playing:
    guess = input("give me your best guess \n")
    if number == guess:
        print("you win the game")
        print("the number was ",number)
        break
    else:
        print("your guess is not queit right, try again")
        