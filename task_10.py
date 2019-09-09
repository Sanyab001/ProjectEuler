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


sum = 0
for i in range(2, 2000):
    if is_simple(i) == True:
        sum += i
print(sum)

# Способ очень долгий, переделать
