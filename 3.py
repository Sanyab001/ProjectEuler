# Простые делители числа 13195 - это 5, 7, 13 и 29.
#
# Каков самый большой делитель числа 600851475143, являющийся простым числом?

import math


def is_simple(number):
    rez = math.ceil(math.sqrt(number))
    l = []
    for i in range(3, rez):
        if number % i == 0:
            if is_simple(i) == []:
                l.append(i)
    return l


rez = is_simple(600851475143)
print(max(rez))

fin = round(600851475143 ** 0.5)

