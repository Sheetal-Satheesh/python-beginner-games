import random

def guess_the_number(x):
    random_number = random.randint(1, x)
    guessed_number = 0
    print("Try to Guess the number Which Computer has Guessed.")
    
    while guessed_number != random_number:
        guessed_number = int(input(f"Guess a number between 1 and {x}:"))
        if guessed_number > random_number:
            print("Try Again, the guessed number is too high.")
        elif guessed_number < random_number:
            print("Try Again, the guessed number is too low.")

    print(f"Hurray!! You have guess the number {random_number} correctly!")

def computer_guess(x):
    print(f"Lets Play! Computer Guess a number between 1 and {x}")
    low = 1
    high = x
    user_feedback = ''
    while user_feedback != "C":
        if low != high:
            guessed_number = random.randint(low, high)
        else:
            guessed_number = high
            break
        user_feedback = input(f"Is the guessed number {guessed_number} too high(H/h) or is it too low (L/l)? Is it correct (C/c)").upper()
        if user_feedback == "L":
            low = guessed_number + 1
        elif user_feedback == "H":
            high = guessed_number - 1
            
    print(f"The computer has guessed your number {guessed_number} correctly!!")

computer_guess(10)


