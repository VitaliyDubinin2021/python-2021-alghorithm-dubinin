""" Задание №2: Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. Выполнить
над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат. """

numb_1 = 5
numb_2 = 6

""" Для справки * - что такое битовые операции:
1. Битовая операция "И" копирует бит в результат, только если бит присутствует
в обоих операндах. """

and_bit = numb_1 & numb_2

print(f"""Битовая операция «И» для чисел {numb_1} ({bin(numb_1)}) и {numb_2} ({bin(numb_2)}):
     {bin(and_bit)} то есть {and_bit}""")

""" 2. Битовая операция "ИЛИ" копирует бит, если тот присутствует в хотя бы в одном
из операндов. """

or_bit = numb_1 | numb_2

print(f"""Битовая операция «ИЛИ» для чисел {numb_1} ({bin(numb_1)}) и {numb_2} ({bin(numb_2)}):
     {bin(or_bit)} то есть {or_bit}""")

""" 3. Битовая операция "Исключительное ИЛИ" копирует бит, только если бит присутствует
в одном из операндов, но не в обоих сразу. """

or_exception_bit = numb_1 ^ numb_2

print(f"""Битовая операция «Исключительное ИЛИ» для чисел {numb_1} ({bin(numb_1)}) и {numb_2} ({bin(numb_2)}):
     {bin(or_exception_bit)} то есть {or_exception_bit}""")

""" 4. Битовая операция "Отрицание" меняет биты на обратные, там где была единица
становиться ноль и наоборот (инверсия). """

inversion_bit_numb_1 = ~numb_1
inversion_bit_numb_2 = ~numb_2

print(f"""Битовая операция «Отрицание» для чисел {numb_1} ({bin(numb_1)}) и {numb_2} ({bin(numb_2)}):
     {bin(inversion_bit_numb_1)} то есть {inversion_bit_numb_1} для числа {numb_1} и
     {bin(inversion_bit_numb_2)} то есть {inversion_bit_numb_2} для числа {numb_2}""")

""" 5. Битовая операция "Побитовый сдвиг вправо". Значение левого операнда получает сдвиг вправо
на количество бит, которые указаны в правом операнде. """

shift_bit_right = numb_1 >> 2  # Значение '2' - биты.

print(f"""Битовая операция «Побитовый сдвиг вправо» для чисел {numb_1} ({bin(numb_1)}) и {numb_2} ({bin(numb_2)}):
     {bin(shift_bit_right)} то есть {shift_bit_right}""")

""" 6. Битовая операция "Побитовый сдвиг влево". Значение правого операнда получает сдвиг влево
на количество бит, которые указаны в правом операнде. """

shift_bit_left = numb_1 << 2  # Значение '2' - биты.

print(f"""Битовая операция «Побитовый сдвиг влево» для чисел {numb_1} ({bin(numb_1)}) и {numb_2} ({bin(numb_2)}):
     {bin(shift_bit_left)} то есть {shift_bit_left}""")
