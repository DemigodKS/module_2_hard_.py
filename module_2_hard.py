import random


def password():
    numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    one_number = random.choice(numbers)
    return one_number


one_number = password()
print("Рандомное число:")
print(one_number)
print("Пароль:")
for i in range(1, one_number):
    for j in range(i, one_number):
        if ((i + j) % one_number == 0 or one_number % (i + j) == 0) and i != j:
            print(f'{i}{j}', end='')

