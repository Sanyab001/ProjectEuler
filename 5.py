# 2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
#
# Какое самое маленькое число делится нацело на все числа от 1 до 20?


# Проверка числа на деление без остатка
def check_devision(n):
    for i in range(2, 21):
        if n % i == 0 and i == 20:
            return True
        elif n % i == 0:
            i += 1
        else:
            return False


# Укажим изначальный статус False и число, с которого начнется проверка
# Результатом должно быть число, которое заканчивается на 0
# Будем проверять числа с шагом +10
def l_number():
    s = False
    num = 20
    while s != 1:
        ck = str(num)
        if ck[-1] == str(0):
            s = check_devision(num)
            if s:
                print(num)
            else:
                num += 10


l_number()
# Ответ 232792560
