# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите
# в формате чч:мм:сс. Используйте форматирование строк.

user_time = int(input('Enter the time in seconds: '))
hours = user_time // 3600
minutes = (user_time - (hours * 3600)) // 60
seconds = (user_time - (hours * 3600)) - (minutes * 60)

print(f'It`s {hours}:{minutes}:{seconds}')
