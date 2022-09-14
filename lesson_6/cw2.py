from random import randint

random_number = randint(1, 15)
print(random_number)
i = 1
run = True

while run == True:
    user_input = int(input("ATTEMPT: #" + str(i) + ". ENTER THE NUMBER: "))
    if user_input == random_number:
        print("You won! attempts: ", i)
        run = False
    else:
        if user_input < random_number:
            print("YOUR NUMBER IS LOWER THAN THE ANSWER")
        elif user_input > random_number:
            print("YOUR NUMBER IS UPPER THAN THE ANSWER")
        i += 1