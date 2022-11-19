row = int(input('Сколько строк в таблице?'))
column = int(input('Сколько столбцов в таблице?'))
# Создаем пустую матрицу
map = []
# Для каждой строки в кол-ве (x)
for i in range(row):
    # Добавляем список с кол-вом столбцов равным (y)
    map.append([0] * column)
# Выводим матрицу построчно
for row in map:
    for column in row:
        print(column, end=' ')
    print()
row = int(input('Какую строку выбрать?'))
column = int(input('Какой столбец?'))
change = int(input('На что заменить?'))
# Присваиваем измененное значение в ячейку по индексу, исходя из введенных данных
map[row - 1][column - 1] = change
# Снова выводим карту построчно
for i in map:
    for j in i:
        print(j, end=' ')
    print()
