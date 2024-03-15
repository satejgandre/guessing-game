import random
def main():
    number = random.randint(0,100)
    while True:
        guess = int(input("Guess: "))
        if guess is number: print("Correct!"); break
        elif guess > number: print("Less...")
        else: print("More...")
    return 1
input("THE PROGRAM HAS FINISHED WITH A STATUS CODE OF {}\nPRESS [ENTER] TO EXIT".format(main()))