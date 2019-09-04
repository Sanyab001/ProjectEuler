# Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-ое простое число - 13.
#
# Какое число является 10001-ым простым числом?

def is_simple_number(number):
    """Проверка числа на простоту"""
    if number == 2:  # Если проверяем число 2, то выводим сразу True
        return True
    elif number % 2 == 0:  # Все четные числа кроме 2 не могут быть простыми
        return False
    else:
        for i in range(2, number):
            if i == number - 1 and number % i != 0:
                return True
            elif number % i != 0:
                i += 1
            else:
                return False


# Создадим счетчик найденных простых чисел, и когда он достигнет нужного значения, вернем это простое число
# Проверять будем с числа 2
def simple_count(count):
    """Функция находит n-ое простое число"""
    active_count = 0
    n = 2
    while count != active_count:
        stat = is_simple_number(n)
        if stat:
            active_count += 1
            if count == active_count:
                return n
            n += 1
        else:
            n += 1


count = 10001
print(count, "простое число:", simple_count(count))
# 10001 простое число: 104743
