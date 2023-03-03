# рекурсивное нахождение факториала
def get_factorial(num):
    if num > 0:
        return num * get_factorial(num - 1)
    else:
        return 1


# рекурсивное нахождение чисел Фибоначчи
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


# for number in range(0, 11):
#     print(fibonacci(number))

# рекурсивное нахождение НОД 2х чисел (решето Эратосфена)
# GCD - greatest common divisor
def gcd(x, y):
    if x % y == 0:
        return y
    else:
        return gcd(x, x % y)


# print(gcd(49, 28))

# функция принимает число и распечатывает числа от 1 до n
def rprint(num):
    if num > 0:
       rprint(num - 1)
       print(num)

# rprint(10)
