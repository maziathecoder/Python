def shut_down(s):
    if s.lower() == "yes":
        return "Shutting down..."
    elif s.lower() == "no":
        return "Shutdown aborted!"
    else:
        return "Sorry, I didn’t understand that."
user_input = input("Do you want to shut down? (yes/no): ")
print(shut_down(user_input))