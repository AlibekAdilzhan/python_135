from random import randint

a = randint(1, 3)

print("Камень ножницы бумага!")
print("Компьютер уже сделал свой выбор")
print("Теперь ваша очередь...")
print("1 --- Камень\n2 --- Ножницы\n3 --- Бумага\n")
b = int(input("Сделайте свой выбор: "))

if a == b:
    print("draw")
elif b - a % 3 == 1:
    print("computer")
else:
    print("human")
