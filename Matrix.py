# Данный скрипт позволяет создать таблицу указанного размера и выводит на экран

rows = int(input('Сколько строк в таблице?'))
columns = int(input('Сколько столбцов в таблице?'))
map = [([0] * columns) for row in range(rows)]
for row in map:  # Выводим таблицу построчно
    for column in row:
        print(column, end=' ')
    print()

# Также скрипт позволяет заменить ячейку в таблице по ее координатам
# Поскольку счет по индексам идет с коэффицента 0, из каждой из координат необходимо вычесть единицу

row_number = int(input('Какую строку выбрать?'))
column_number = int(input('Какой столбец?'))
change = int(input('На что заменить?'))
map[row_number - 1][column_number - 1] = change
for row in map:  # Выводим измененную таблицу построчно
    for column in row:
        print(column, end=' ')
    print()
