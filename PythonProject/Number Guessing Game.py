import random

print("Welcome to Number Guessing Game!")
print("I'm Thinking of number between 1 and 100")
level = input("Choose a dificulty: Type 'easy' or 'hard': ")

chosen_number = random.randint(1, 100)
print(chosen_number)

attemps = 0

if level == "easy":
    attemps = 10
    print(f"You have {attemps} remaining to make a guess.")
else:
    attemps = 5
    print(f"You have {attemps} remaining to make a guess.")

while attemps > 0:
    guess = int(input("Make a guess: "))

    if guess == chosen_number:
        print("You got it")
        attemps = 0
    elif guess > chosen_number:
        attemps -= 1
        print("Too high")
        print("Guess again")
        print(f"You have {attemps} remaining to make a guess.")
    elif guess < chosen_number:
        attemps -= 1
        print("Too low")
        print(f"You have {attemps} remaining to make a guess.")
        print("Guess again")

