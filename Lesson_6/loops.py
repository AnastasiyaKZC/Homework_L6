import random
# в питоне два вида циклов

# 1. While - цикл с предусловием
# пока пользователь не введет правильный номер, ...

# while True:
#     print("I'm teapot!") - бесконечно раз будет выполнятся, нет условия выхода


required_number = 7
user_number = random.randint(0, 10)

while required_number != user_number:
    user_number = random.randint(0, 10)
    print(f"Пользователь ввел число {user_number}") #условие выхода



iterations_count = 10 # - цикл с определенным количеством итераций
i = 0 # изначальное значение

while i < iterations_count:
    print(f"Текущая итерация: {i}")
    i += 1
    # i = i + 1 - полная запись выражения выше


# цикл For. Итерируем списки и словари

users = [
    {"name": "Oleg", "age": 32},
    {"name": "Sergey", "age": 24},
    {"name": "Stanislav", "age": 15},
    {"name": "Olga", "age": 45},
    {"name": "Maria", "age": 18},
]

from pprint import pprint #Функция pprint() автоматически форматирует данные, делая их более читаемыми.


for user in users:
    pprint(f"Пользователю {user['name']} {user['age']} лет")


d = {
    "first": 1,
    "second": 2,
    "third": 3
}

for item in d:
    pprint(item) # такой цикл только по ключам


for item in d.keys():
    pprint(item)

for item in d.values():
    pprint(item) # такой цикл только по значениям


for item in d.items():
    pprint(item)  # такой цикл выводит ключ и значение


for key, value in d.items():
    print(f"Ключ: {key}, Значение: {value}")


# 2. for i in range - цикл с итератором


# print(list(range(5, 15, 2)))


iterations_count = 10


for i in range(3, iterations_count, 2):
    print(f"Текущая итерация: {i}")


# Break/Continue/Else - прерывание цикла

for i in range(iterations_count):
    if i % 2 == 0:
        continue
        print("Я никогда не выполнюсь")

    if i > 7:
        break

    print(f"Точно нечетное число: {i}")

for i in range(5):
    for j in range(5):
        print(i, j)
        if j == 3:
            continue

        if j == 4:
            break

    if i % 2 == 0:
        continue

# enumerate - возвращает пары (индекс, значение)


cities = ["Екатеринбург", "Москва", "Сочи"]


for i, city in enumerate(cities):
    print(f"{city} на {i + 1} месте по загрязнению воздуха")