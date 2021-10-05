""" Задание №5. Пользователь вводит две буквы. Определить, на каких местах алфавита они
стоят и сколько между ними находится букв. """

first_letter, second_letter = [
    letter for letter in input('Здравствуйте! Введите две буквы на русском языке в нижнем'
                               ' регистре через пробел: ').split()
]

our_list = [chr(p) for p in range(ord('а'), ord('я') + 1)]

letter_index_1 = our_list.index(first_letter) + 1
letter_index_2 = our_list.index(second_letter) + 1

if letter_index_1 < letter_index_2:
    advance = 1
else:
    advance = -1

print(f'Первая буква {first_letter}, введенная Вами, находится на позиции: {letter_index_1}')
print(f'Вторая буква {second_letter}, введенная Вами, находится на позиции: {letter_index_2}')

print(f'Между введенными Вами буквами {first_letter} и {second_letter} находятся буквы '
      f'{our_list[letter_index_1 - 1 + advance:our_list.index(second_letter):advance]}')

