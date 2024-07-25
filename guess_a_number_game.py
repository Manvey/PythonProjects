from random import randint

EASY_LEVEL_TURNS = 10
MEDIUM_LEVEL_TURNS = 7
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
    """check answer from guess. return number of turns remaining"""
    if guess > answer:
        print("Too High")
        return turns - 1
    elif guess < answer:
        print("Too Low")
        return turns -1
    else:
        print(f"You got it! The answer was {answer}")

def set_difficulty():
    level = input("Choose difficulty. Type 'easy' or 'medium' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "medium":
        return MEDIUM_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    """Choosing random number between 1 to 100."""
    print("Welcome to the Number Guessing Game!!")
    print("I'm thinking of a number between 1 to 100.")
    answer = randint(1, 100)

    turns = set_difficulty() 
    guess = 0
    while guess != answer:
        print(f"You have {turns} turns remaining to guess the number.")

        # Let the user guess the number
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        
        if turns == 0:
            print(f"You've run out of guesses. You lose.")
            print("Better luck next time!")
            print(f"The answer was {answer}.")
            return
        elif guess != answer:
            print("Guess Again.")

game()


