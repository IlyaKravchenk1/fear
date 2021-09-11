res = {}
for n in range(2, 10):
    res[n] = []
    for f in range(2, 100):
        if f % n == 0:
            res[n].append(f)
    print(
        f'Для числа {n} кратны - {len(res[n])}. Кратные числа: {res[n]}.'
        )
