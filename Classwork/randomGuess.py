import random

my_guess = (random.randint(100, 1000))

count = 0
while   count <3:
        your_guess = int(input('enter your guess'))
        if          my_guess != your_guess :
             print('try again')
        else :
             print('correct',my_guess)

             break
        count +=1
else :
     print("you cant make it",my_guess)


