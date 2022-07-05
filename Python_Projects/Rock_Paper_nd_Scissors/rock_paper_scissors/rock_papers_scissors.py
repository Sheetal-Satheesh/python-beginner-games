import random

def play():
    user_input = input(" Enter your choice 'r' for rock,'p' for paper ,'s' for scissors \n").lower()
    computer_input = random.choice(['r', 'p', 's'])
    print(f"Computers Choice:{computer_input}")

    if user_input == computer_input:
        return 'This is a Draw'

    if is_win(user_input, computer_input):
        return "You Win"

    return "You Lost"

def is_win(player, opponent):
    if(player == "r" and opponent == "s"):
        return True
    elif(player =="s" and opponent == "p"):
        return True
    elif(player == "p" and opponent == "r"):
        return True

print(play())