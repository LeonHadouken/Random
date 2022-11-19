count_digits = 0
summary = 0
multiply = 1
maximum_digit = 0
minimum_digit = 9
number = int(input('Введите число'))
saved_number = number

while number > 0:
    last_digit = number % 10
    count_digits += 1
    summary += last_digit
    multiply *= last_digit
    if last_digit > maximum_digit:
        maximum_digit = last_digit
    if last_digit < minimum_digit:
        minimum_digit = last_digit
    number = number // 10  # Отделить последнюю цифру от числа.

print(f'кол-во цифр в числе {saved_number} = {count_digits}')
print(f'сумма цифр в числе {saved_number} = {summary}')
print(f'произведение цифр в числе {saved_number} = {multiply}')
print(f'наибольшая цифра {maximum_digit}')
print(f'наименьшая цифра {minimum_digit}')
