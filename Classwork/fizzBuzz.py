# a number that prints 1-100
# when it can be divided by 3 print fizz
# when it can be divided by 5 print fizzbuzz

num = 1

for num in range(1,101):

    if num % 15 == 0:
        print("fizzbuzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    elif num % 3 or num % 5 == 0:
        print(num)
