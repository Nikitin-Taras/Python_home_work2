# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

num = int(input('Введите трехзначное число:'))

a = int(num / 100)
b = num // 10 % 10
c = num % 10
sum = a + b + c

print(num, '-> ', sum, '(', a, b, c, ')') 