dublicate_test = []
clear_list = []
list_size = int(input('Введите коли-во элементов'))
buffer_string = ''

for i in range(list_size):
    dublicate_test.append(input('Введите элемент списка'))
for i in dublicate_test:
    if i not in clear_list:
        clear_list.append(i)
        buffer_string += (f'{i} встретилось {dublicate_test.count(i)} раз(а) \n')
print('Все элементы списка:', end=' ')
for i in dublicate_test:
    print(i, end=' ')
print()
print(buffer_string)
print(f'Список без дубликатов {clear_list}')
