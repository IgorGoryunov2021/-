# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

# Так и не разгадал как сделать, чтобы программа всчитала самое маленькое число. 

num_init = int(input('Введите целое положительное число:'))
greatest_dig = 0
num = num_init

while num > 0:
    digit = num % 10
    if digit > greatest_dig:
        greatest_dig = digit
        if greatest_dig == 9:
            break
    num = num // 10
print(f'Наибольшая цифра в числе {num_init} равна {greatest_dig}')
