#2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

second = int(input("Введите время в секундах"))
translation_into_hours = 0.000278
hours_time_period = second * translation_into_hours
#print("В часах это будет", hours_time_period, "часа")
translation_into_minutes = 0.0166667
minutes_time_period = second * translation_into_minutes
#print("В минутах это будет", minutes_time_period, "минут")

seconds_time_period = second
#print("В секундах это будет", seconds_time_period, "секунд")

print("{:.0f}:{:.0f}:{:.0f}".format(hours_time_period, minutes_time_period, seconds_time_period))

#print("{:.0f} :".format(minutes_time_period))
#print("{:.0f} :".format(seconds_time_period))

