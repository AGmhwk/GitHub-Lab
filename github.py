<<<<<<< HEAD
import random  # used to generate a random number

# function to calculate score based on number of guesses
def score(guesses):
    if guesses <= 5:
        return "Amazing! You scored 100 points!"
    elif guesses <= 7:
        return "Nice! You scored 75 points!"
    elif guesses <= 10:
        return "You scored 50 points!"
    else:
        return "Sorry! no points for you!"

guess_count = 0  # keeps track of how many guesses the user makes

answer = random.randint(1, 1000)  # generates a random number between 1 and 1000

# main game loop (runs until user guesses correctly)
while True:
    user_num = int(input("Guess a number from 1 to 1000: "))  # user input
    guess_count += 1  # increase guess count each time

    if user_num > answer:
        print("Too high!")  # guess is higher than the answer
    elif user_num < answer:
        print("Too low :(")  # guess is lower than the answer
    else:
        # correct guess
        print(f"Congrats you guessed it! It took you {guess_count} tries.")
        
        # show score using the function
        print(score(guess_count))
        break  # exit the loop when correct

print("end")  # game finished

# extra function (just an example function your partner added)
def multiply(a, b):
    return a * b

print(multiply(2, 3))  # prints 6
=======
import random #getting random
guess_count = 0 #amount of user guesses
answer = random.randint(1,1000) #generating a random answer
while True:
    user_num = int(input("Guess a number from 1 to 1000 "))
    guess_count += 1
    if user_num > answer:
        print("Too high!")
    elif user_num < answer:
        print("Too low :(")
    else:
        print(f"Congrats you guessed it! It took you {guess_count} tries.")
        guess_count = 0
        again = input("would you like to try again? ")
        if again.lower() == "yes":
            answer = random.randint(1,1000)
        elif again.lower() == "no":
            print("thanks for playing")
            break
        else:
            break
            
    
print("end")
#Zohra
def multiply(a, b):
    return a * b
print(multiply(2, 3))
>>>>>>> 3f080797b3a762510e93cf329440306238dba37b
