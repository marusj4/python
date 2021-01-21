#Task2
#Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды
# выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time_in_seconds = int(input('Введите время в секундах: '))
seconds = time_in_seconds % 60
#перевели секунды в минуты
time_in_minutes = time_in_seconds // 60
#Минуты- остаток от деления
minutes = time_in_minutes % 60
# Часы- целые значения
hours = time_in_minutes // 60

print('%d:%d:%d' % (hours, minutes, seconds ))
