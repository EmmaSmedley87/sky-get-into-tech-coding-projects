import random

# user guesses the number
def guess(x):
    randomNumber = random.randint(1, x)
    guess = 0
    while guess != randomNumber:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        # add if statements to add computer feedback on guess
        if guess < randomNumber:
            print("Sorry, guess again. Too Low.")
        elif guess > randomNumber:
            print("Sorry, guess again. Too high.")
    print(f"Yay, you have guessed the number {randomNumber} correctly!")

guess(10)

# computer guesses the number

def computerGuess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randit(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess}too high (H), too low (L), or correct (C)")
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"Yay the computer guessed your number, {guess} correctly!")
