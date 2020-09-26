""" 25.9.20
author-manas verma
we have to make a program which  will
... give some amount of chances to the user to guess the number.
... we will give number 14 to guess.
... print no. of guesses left
... we will give 5 chances to guess the number.
... over the game after 5 chances"""
n = 14
number_of_guesses = 1
print("welcome to this game, you have to guess a number. \n you have only 5 chances to guess the number")
while(number_of_guesses<=5):
    num1 = int(input("guess the number\n"))
    if (num1 < 14):
        print("you have guessed wrong number, the right number is greater :(")
    elif (num1 > 14):
        print("you guessed the wrong number, the right number is lesser than this :(")
    else:
        print("congratulation you have guessed a right number :)")
        print(number_of_guesses, "no. of guesses he took to finish.")
        break
    print(5-number_of_guesses, "no. of guesses left")
    number_of_guesses = number_of_guesses + 1

if (number_of_guesses>5):
    print("game over, right number is 14")





