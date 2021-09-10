#8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

n = int(input('Введите кол-во чисел: '))
num = ''
for i in range(n):
    buf_num = input("Число: ")
    num += buf_num
print(num)

digit = int(input('Введите цифру для подсчета: '))
counter = 0
NUM = int(num)
while NUM!=0:
    reminder = NUM%10
    if reminder == digit:
        counter +=1
    NUM = NUM//10

print(f'Заданная цифра повторяется {counter} раз')