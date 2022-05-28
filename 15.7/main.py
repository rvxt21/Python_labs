"""15.7
Описати клас Двохбайтне ціле число для роботи з цілими числами,
представленими двома байтами. Інтервал представлення при цьому – від -215
(-32768) до 215-1 (32767). Операції не можуть вивести за межі інтервалу
представлення. Наприклад, 32767 + 1 == -32768, 32767 + 2 == - 32767 і т.д.
Якщо результат операції виводить за межі інтервалу представлення, повинна
ініціюватися помилка переповнення.
Перевизначити у цьому класі операції +, -, *, //, %.
Описати також 3 класи обробки помилок для двохбайтних цілих чисел:
загальний клас обробки помилок та два його підкласи для обробки помилки
переповнення та помилки ділення на 0.
Використати цей клас для розв’язання задач:
а) обчислення n!
б) обчислення x
n
, де x – ціле, n – невід’ємне ціле.
Забезпечити обробку помилок при виконанні обчислень."""

class DefaultException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'DefaultException, {0}'.format(self.message)
        else:
            return 'DefaultException'


class DividingByZero(DefaultException):
    def __str__(self):
        if self.message:
            return 'Dividing by Zero, {0}'.format(self.message)
        else:
            return 'Dividing by Zero'


class Overflow(DefaultException):
    def __str__(self):
        if self.message:
            return 'Overflow, {0}'.format(self.message)
        else:
            return 'Overflow'


class int_16:
    def __init__(self, value):
        self.max = 32767
        self.min = -32768
        if value <= self.max and value >= self.min:
            self.value = value
        else:
            raise Overflow

    def __add__(self, other):
        sum = self.value + other.value
        return int_16(sum)

    def __sub__(self, other):
        sub = self.value - other.value
        return int_16(sub)

    def __mul__(self, other):
        mul = self.value * other.value
        return int_16(mul)

    def __floordiv__(self, other):
        if other.value == 0:
            raise DividingByZero
        else:
            return int_16(self.value // other.value)

    def __mod__(self, other):
        if other.value == 0:
            raise DividingByZero
        else:
            return int_16(self.value % other.value)

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value


def factor(num):
    if num == int_16(0):
        return int_16(1)
    else:
        return num * factor(num - int_16(1))


if __name__ == '__main__':
    A = int_16(100)
    B = int_16(2)
    # print(A%B)

    print((A * B).value)
    try:
        print(factor(A).value)
    except Exception as e:
        print(e)