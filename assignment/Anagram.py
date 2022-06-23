number = int(input("enter a number: "))
num_sqr = str(number * number)
length = len(num_sqr)
if str(number) == num_sqr[-1:] or str(number) == num_sqr[-2:]:
    print("Number is Anagram")
else:
    print("Number isn't Anagram")