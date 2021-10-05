""" Задание №3: По введенным пользователем координатам двух точек вывести уравнение прямой
вида y=kx+b, проходящей через эти точки. """

our_coordinates = input('Здравствуйте! Введите координаты двух точек x1, x2, y1 и y2 через пробел: ').split()

print('Введенные координаты x1, x2, y1 и y2 соответственно:', our_coordinates)

x1, x2, y1, y2 = [int(x) for x in our_coordinates]
k = (y1 - y2) / (x2 - x1) # Вычисляем коэффициент К
b = y1 - k * x1

print(f'Уравнение прямой для координат x1, x2, y1, y2 принимает вид: y = {k}x + {b}')
