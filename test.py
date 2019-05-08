import math


def one():
    weight, height = eval(input())
    bmi = weight / math.pow(height, 2)
    print('YOU BMI IS %d' % bmi)
    result = 'too thin' if bmi <= 18.5 else ('normal' if bmi <= 23.9 else ('overweight' if bmi <= 27.9 else 'fat'))
    print(result)


# one()


def two():
    for i in range(0, 320, 20):
        k = 5 / 9 * (i - 32)
        print('f=%d,c=%d' % (i, k))
        i += 20


# two()


def there():
    n = eval(input())
    if n <= 0:
        print('Please enter a positive integer')
        return
    k = 0
    while k != 1:
        if n % 2 == 0:
            print('%d / 2 = %d' % (n, n // 2))
            k = n = n // 2
        else:
            print('%d * 3 + 1 = %d' % (n, n * 3 + 1))
            k = n = n * 3 + 1


# there()


def four():
    n = eval(input())
    s = k = 1
    for i in range(2, n + 1):
        k *= i
        s += k
    print(s)


# four()


def five():
    for i in range(1, 5):
        for k in range(1, 5):
            for j in range(1, 5):
                if i != k & i != j & k != j:
                    print(i * 100 + k * 10 + j)


# five()

