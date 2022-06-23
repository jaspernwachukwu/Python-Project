import random

correct_guess= random.randint(0,100)
count=0
while count<5:
    guess= int(input("enter your guess: "))
    if guess<0 or guess > 100 :
       print("out of range")
       break

    if guess < correct_guess:
        print("too low,try again")
    elif guess > correct_guess:
        print("too high try again")
    else:
        print("you're correct",correct_guess)
        break
    count +=1
else:
    print("you can never make it")
    print("the correct answer is", correct_guess)

