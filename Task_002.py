# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint
n = int(input('Введите количество элементов массива: ')) # Объявляем переменную количество элементов массива
specified_array = [] # Объявляем массив
for i in range(n): # Объявляем цикл заполнения списка
    specified_array.append(randint(-20, 20)) # Заполненяем список числами от -20 до 20
print(specified_array)
min_value = int(input('Введите минимальное значение: '))
max_value = int(input('Введите максимальное значение: '))
for i in range(len(specified_array)):
    if min_value <= specified_array[i] <= max_value:
        print(i)





