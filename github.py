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
        guess_count = 0
        print(f"Congrats you guessed it! It took you {guess_count} tries.")
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
