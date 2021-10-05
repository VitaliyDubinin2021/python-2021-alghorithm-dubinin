""" Задание №8: Определить, является ли год, который ввел пользователь,
високосным или невисокосным. """

required_year = int(input('Здравствуйте! Введите год: '))

if required_year % 400 == 0:
    print('Введенный Вами', required_year, 'год является високосным!')
elif required_year % 100 == 0 and required_year % 400 != 0:
    print('Введенный Вами', required_year, 'год является невисокосным!')
elif required_year % 4 == 0:
    print('Введенный Вами', required_year, 'год является високосным!')
else:
    print('Введенный Вами', required_year, 'год является невисокосным!')

# Для справки * - високосным является тот год, номер которого будет кратен 400 годам.
# Для справки * - остальные годы, номер которых будет кратен 4 годам, являются високосными.
# Для справки * - остальные года, номер которых будет кратен 100 годам, являются невисокосными.

