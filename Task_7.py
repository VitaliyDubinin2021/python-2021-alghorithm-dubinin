""" Задание №7: По длинам трех отрезков, введенных пользователем,
определить возможность существования треугольника, составленного из этих отрезков.
Если такой треугольник существует, то определить, является ли он разносторонним,
равнобедренным или равносторонним. """

lenght_1 = input('Здравствуйте! Введите длину первого отрезка: ')
lenght_2 = input('Введите длину второго отрезка: ')
lenght_3 = input('Введите длину третьего отрезка: ')

if lenght_2 < lenght_1 + lenght_3 or lenght_1 < lenght_2 + lenght_3 or lenght_3 < lenght_2 + lenght_1:
    if lenght_1 == lenght_2 and lenght_1 == lenght_3:
        print('Отрезки с введенными длинами могут образовать равносторонний треугольник!')
    elif lenght_1 == lenght_2 or lenght_2 == lenght_3 or lenght_1 == lenght_3:
        print('Отрезки с введенными длинами могут образовать равнобедренный треугольник!')
    else:
        print('Отрезки с введенными длинами могут образовать разносторонний треугольник!')
else:
    print('Отрезки с введенными длинами не могут образовать треугольник!!!')
