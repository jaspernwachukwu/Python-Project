river='mississippi'
target= input("input a characteristic to find: ")
for index,letter in enumerate(river):
    if letter==target:
        print("letter found at index:",index)
        break
else:
    print('letter', target,'not found in', river)