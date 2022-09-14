from random import randint

random_number = randint(1, 9)
user_input = int(input("Попытка #1. Введите число: "))

if random_number == user_input:
    print("Угадали")
else:
    print("Не угадали, но у вас еще есть две попытки")
    user_input = int(input("Попытка #2. Введите число: "))
    if random_number == user_input:
        print("Угадали")
    else:
        print("Не угадали, но у вас есть еще одна попытка")
        user_input = int(input("Попытка #3. Введите число: "))
        if random_number == user_input:
            print("Угадали")
        else:
            print("Не угадали")
            print("Попытки закончились")