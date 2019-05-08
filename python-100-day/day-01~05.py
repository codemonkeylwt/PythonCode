import math


# 寻找指定范围内的水仙花数
def find_narcissistic_number(min, max):
    if len(str(min)) != 3 or len(str(max)) != 3:
        print("水仙花数必须为三位数")
        return
    print("%s 到 %s 的水仙花数有:" % (min, max))
    for i in range(min, max + 1):
        a = i % 10
        b = int(i / 10) % 10
        c = int(i / 100) % 10
        if (math.pow(a, 3) + math.pow(b, 3) + math.pow(c, 3)) == i:
            print(i, end=" ")
    print("\n\r==================================================")


find_narcissistic_number(100, 500)


# 求范围内的所以完美数
def perfect_number(min, max):
    if min <= 0:
        print("最小值必须大于零")
        return
    print("%s 到 %s 的完美数有:" % (min, max))
    for num in range(min, max + 1):
        sum = 0
        for i in range(1, int(math.sqrt(num)) + 1):
            if num % i == 0:
                sum += i
                if i > 1 and num / i != num:
                    sum += num / i
        if sum == num:
            print(num, end=" ")
    print("\n\r==================================================")


perfect_number(1, 500)


# 百钱买百鸡
def hundred_chicken():
    for x in range(0, 21):
        for y in range(0, 34):
            z = 100 - x - y
            if 5 * x + 3 * y + z / 3 == 100:
                print("公鸡%s只，母鸡%s只，小鸡%s只。" % (x, y, z))
    print("==================================================")


hundred_chicken()


# 打印斐波那契数列的第N项
def fibonacci_sequence(num):
    a = 0
    b = 1
    for _ in range(num):
        (a, b) = (b, a + b)
        print(a, end=" ")
    print("\n\r斐波那契数列第%s项为：%s" % (num, calculate(num)))
    print("==================================================")


def calculate(num):
    if num == 1 or num == 2:
        return 1
    else:
        return calculate(num - 1) + calculate(num - 2)


fibonacci_sequence(10)
