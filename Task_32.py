# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

MinValue = int(input("Минимальный элемент "))
MaxValue = int(input("Максимальный элемент "))

l = [randint(1, 100) for _ in range(20)]
indexes = []
for i in range(len(l)):
    if MinValue <= l[i] <= MaxValue:
        indexes.append(i)

print(l)
print(indexes)