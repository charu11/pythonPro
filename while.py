
i = 1
while i <= 10:
    print(i)
    i += 1

print("done with the while loop")


secret_word = "arsenal FC"
guess = ""
guess_count = 0
guess_limit = 5
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("enter the guess:")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("out of moves")
else:
    print("you win")