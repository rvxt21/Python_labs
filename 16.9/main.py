"""16.9
Нехай елементи послідовності seq можна впорядкувати за зростанням
(неспаданням). Описати клас-ітератор, який проходить всі елементи
послідовності seq, повертаючи елементи у порядку
а) зростання
б) спадання
Сама послідовність seq повинна залишатись незмінною."""

seq = [5, 5, 10, 2, 1, 3, 3, 8]

class Task:
    def __init__(self, seq):
        self.seq1 = seq
        self.seq1.sort()

    def __iter__(self):
        self.n = -1
        return self
    def __next__(self):
        self.n+=1
        if self.n < len(self.seq1):
            result = self.seq1[self.n]
            return result
        else:
            raise StopIteration

class TaskB:
    def __init__(self, seq):
        self.seq1 = seq
        self.seq1.sort(reverse = True)

    def __iter__(self):
        self.n = -1
        return self
    def __next__(self):
        self.n+=1
        if self.n < len(self.seq1):
            result = self.seq1[self.n]
            return result
        else:
            raise StopIteration

#a = Task(seq)
#for i in a:
    #print(i)
b=TaskB(seq)
for i in b:
    print(i)

