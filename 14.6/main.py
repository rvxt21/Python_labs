""" За допомогою стандартного контейнера deque розв’язати задачу:
По колу розташовано n гравців з номерами від 1 до n. У лічилці m слів.
Починають лічити з першого гравця. m-й за ліком вибуває. Потім знову
лічать з наступного гравця за вибулим. Знову m-й вибуває. Так продовжують,
поки не залишиться жодного гравця. Треба показати послідовність номерів,
що вибувають, при заданих n та m.
"""
from collections import deque
from ctypes import pointer


def main():
    n = input("Put n\n")
    m = int(input("Put m\n"))
    player = deque()
    for i in range(int(n)+1):
        player .append(i)
    player .popleft()
    #print(player )
    pointer = 0
    print("Result:")
    while len(player ) > 0:
        if len(player ) == 1:
            print(player [0])
            break
        pointer += m
        while pointer  >= len(player ):
            pointer = pointer - len(player )
        print(f'{player [pointer]}, ')
        del player [pointer]

if __name__ == "__main__":
    main()
