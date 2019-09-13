# Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.
#
# Найдите сумму всех простых чисел меньше двух миллионов.


def is_simple(number):
    """Проверка числа на простоту"""
    if number == 1 or number == 2:
        return True
    elif number % 2 == 0:
        return False
    else:
        for n in range(2, number):
            if number % n == 0:
                return False
            elif n == number - 1 and number % n != 0:
                return True
            else:
                False


def eratosthenes(n):  # Конечное число списка
    simple = list(range(n + 1))
    simple[1] = 0
    for i in simple:
        if i > 0:
            for j in range(i + i, len(simple), i):
                simple[j] = 0
    return simple


result = 0
for n in eratosthenes(2000000):
    result += n

print(result)
# Ответ 142913828922
