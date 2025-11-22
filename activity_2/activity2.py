import random
while True:
    user_action = input("enter a choice(rock, paper, scissors): ")
    possible_action = ["rock","paper","scissors"]
    computer_action = random.choice(possible_action)
    print(f"\nyou choose {user_action},computer choose {computer_action}.\n")
    if user_action == computer_action:
        print("its a tie")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("rock smashes scissors!! you win")
        else:
            print("paper covers rock!! you lose")
    elif user_action == "paper":
        if computer_action == "rock":
            print("paper covers rock!! you win")
        else:
            print("scissors cuts paper!! you lose")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("scissors cuts paper!! you win")
        else:
            print("rock smashes paper!! you lose")
    play_again = input("paly again?(y/n): ")
    if play_again != "y":
        break