x = int(input('Сколько строк в таблице?'))
y = int(input('Сколько столбцов в таблице?'))
# Создаем пустую матрицу
map = []
# Для каждой строки в кол-ве (x)
for i in range(x):
    # Добавляем список с кол-вом координат равным (y)
    map.append([0] * y)
# Выводим матрицу построчно
for i in map:
    print(i)
x = int(input('Какую строку выбрать?'))
y = int(input('Какой столбец?'))
change = int(input('На что заменить?'))
# присваиваем измененное значение в ячейку по индексу, исходя из введенных данных
map[x - 1][y - 1] = change
# Снова выводим карту построчно
for i in map:
    print(i)


