count_digits = 0  # счетчик цифр в числе
summary = 0  # сумма всех цифр в числе
multiply = 1  # произведение всех цифр в числе
maximum_digit = 0  # наибольшая цифра в числе
minimum_digit = 9  # наименьшая цифры в числе
number = int(input('Введите число'))
saved_number = number

while number > 0:
    last_digit = x % 10
    count_digits += 1
    summary += last_digit
    multiply *= last_digit
    if last_digit > maximum_digit:
        maximum_digit = last_digit
    if last_digit < minimum_digit:
        minimum_digit = last_digit
    x = x // 10  # Отделить последнюю цифру от числа.

print(f'кол-во цифр в числе {saved_number} = {count}')
print(f'сумма цифр в числе {saved_number} = {summary}')
print(f'произведение цифр в числе {saved_number} = {multiply}')
print(f'наибольшая цифра {maximum_digit}')
print(f'наименьшая цифра {minimum_digit}')
