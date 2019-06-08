print("Think of a number between 1 and 100")
ans = ""
ceiling = 101
floor = 1
num_guesses = 1

while ans is not "y":
    guess = int((ceiling+floor)/2)
    ans = input("Is your number %d? (y/h/l)" % (guess))
    if ans == "y":
        print("I won in only %d guesses!" % (num_guesses))
    elif ans == "l":
        ceiling = guess
    elif ans == "h":
        floor = guess
    num_guesses += 1
