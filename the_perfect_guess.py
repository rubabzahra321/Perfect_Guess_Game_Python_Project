import random

# 1‑100 random number
target = random.randint(1, 100)

user_input   = None
no_of_guesses = 0

while True:
    no_of_guesses += 1
    try:
        user_input = int(input("👀  Guess the number (1‑100): "))
    except ValueError:
        print("⚠️  Please enter an integer.")
        continue

    if user_input > target:
        print("🔻 Too high! Try something LOWER.")
    elif user_input < target:
        print("🔺 Too low! Try something HIGHER.")
    else:
        print(f"🎉 Correct! You guessed it in {no_of_guesses} tries.")
        break
