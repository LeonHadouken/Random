rows = int(input('Сколько строк в таблице?'))
columns = int(input('Сколько столбцов в таблице?'))
map = []  # Создаем пустую матрицу
for i in range(rows):
    map.append([0] * columns)
for rows in map:  # Выводим карту построчно
    for columns in rows:
        print(columns, end=' ')
    print()
rows = int(input('Какую строку выбрать?'))
columns = int(input('Какой столбец?'))
change = int(input('На что заменить?'))
map[rows - 1][columns - 1] = change
for rows in map:  # Снова выводим карту построчно
    for columns in rows:
        print(columns, end=' ')
    print()
