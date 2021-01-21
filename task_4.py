#Task4
# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

#1способ
number = int(input('Введите число:'))
max_digit = -1
while number != 0:
    #Выделяем последнюю цифру, как остаток от деления
    last_digit = number % 10
    if last_digit > max_digit:
        max_digit = last_digit
    #Делаем сдвиг на одну позицию без посл.цифры
    number = number // 10
print(max_digit)

#2 способ
number_1 = input('Введите число:')
list_numbers = list(number_1)
print(max(list_numbers))





