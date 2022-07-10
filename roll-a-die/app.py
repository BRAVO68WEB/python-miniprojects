import random
while True:
    print('''
          1. Roll \n
          2. Exit ''')
    user = int(input("Choose :- "))
    if user == 1:
        number = random.randint(1, 6)
        print("you got", number)
    else:
        break