#3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

name = input("Как вас зовут? ")
print("Привет,", name)
number = int(input("Теперь введи число "))



print(name,"ваше число", number)
print("Теперь сплюсуем ваше число", number)
sum_of_numbers = number + 10 + 100 + 1000
print("Получилось число:", sum_of_numbers)
#number = int(input("Снова введите число "))
#print(name,"теперь вычтем из вашего числа", number)
#sum_of_numbers_minus = number - 10 - 100 - 1000
#print("Получилось число:", sum_of_numbers_minus)
