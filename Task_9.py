""" Задание №9: Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого). """

number_1 = input('Здравствуйте! Введите первое число: ')
number_2 = input('Введите второе число: ')
number_3 = input('Введите третье число: ')

if number_3 > number_1 > number_2 or number_2 > number_1 > number_3:
    print('Средним числом является', number_1)
elif number_1 > number_2 > number_3 or number_3 > number_2 > number_1:
    print('Средним числом является', number_2)
else:
    print('Средним числом является', number_3)
