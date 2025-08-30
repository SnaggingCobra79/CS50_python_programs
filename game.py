import random

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass
win = random.randint(1,level)
while True:
    try:

        guess = int(input("Guess: "))
        if guess > 0:
            if win == guess:
                print("Just right!")
                break
            elif guess < win:
                print("Too small!")
                continue
            elif guess > win:
                print("Too large!")
                continue
    except ValueError:
        continue
