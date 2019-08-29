# Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона

def fib():
    fib_list = [1, 2, 3]
    while fib_list[-1] + fib_list[-2] < 4000000:
        res_fib = fib_list[-1] + fib_list[-2]
        fib_list.append(res_fib)
    result = 0
    for f in fib_list:
        if f % 2 == 0:
            result += f
        else:
            f += 1
    return result


print(fib())
