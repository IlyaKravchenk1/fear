import random

ra = [random.randint(0, 99) for _ in range(10)]
print(f'Первый массив {ra}')
index_even = []

for n in ra:
    if n % 2 == 0:
        index_even.append(ra.index(n))

print(f'Индексы чётных элементов первого массива: {index_even}')