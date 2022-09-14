from random import randint

run = True 

p1 = "У вас будет отличный день"
p2 = "Вы выиграете приз"
p3 = "Вы поедете на работу"
p4 = "Приедут гости"

while run:
    b = int(input("Режим (1/2): "))
    print("---------------------------------")
    print("Выбрали режим: ", b)
    if b == 1:
        random_p = randint(1, 4)
        if random_p == 1:
            print(p1)
        elif random_p == 2:
            print(p2)
        elif random_p == 3:
            print(p3)
        elif random_p == 4:
            print(p4)
    elif b == 2:
        random_p = randint(1, 2)
        question = input("Задайте вопрос: ")
        if random_p == 1:
            print("Yes")
        else:
            print("No")

    answer = input("Хотите продолжить? (Да\Нет): ")
    if answer.lower() == "да":
        continue
    elif answer.lower() == "нет":
        run = False