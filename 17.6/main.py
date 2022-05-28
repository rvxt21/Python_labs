"""17.6
Побудувати декоратор, який перевіряє, чи містить функція, що
декорується, тільки позиційні параметри. Якщо ні, то ініціює виключення. За
допомогою декоратора розв’язати задачу: скласти підпрограму зі змінною
кількістю параметрів для обчислення функції"""

import inspect


def decorator(func):
    res = inspect.getfullargspec(func)

    def inner(*args, **kwargs):
        if res.varargs != None:  # if it takes not only positional arguments
            func(*args, **kwargs)

        else:
            raise Exception("The function takes positional params only!")

    return inner


@decorator
def fun(*args):
    max_el = max(args)
    sum_ = sum(args)
    if (max_el > sum_):
        print(1)
        return 1
    else:
        print(0)
        return 0


@decorator
def aboba(a, b, c):  # func with positional arguments only
    print("Hello")


if __name__ == "__main__":
    try:
        fun(1, -2, -3, 4)  # returns 1
        fun(1, 2, 3, 4)  # returns 0
        aboba(1, 2, 3)
    except Exception as e:
        print(e)