# 4) Реализуйте базовый класс ​ Car​ . У данного класса должны быть
# следующие атрибуты:speed​,color, name , is_police ​ (булево).
# А также методы: go​ , stop , turn(direction) , которые должны
# сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed​, который должен показывать текущую скорость
# автомобиля. Для классов TownCar и WorkCar ​ переопределите метод ​ show_speed​.
# При значении скорости свыше 60(TownCar) и 40 (WorkCar) должно выводиться сообщение
# о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car():
    def __init__(self,speed, color, name, is_police ):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('The car started.')

    def stop(self):
        print('The car stopped.')

    def turn(self, direction):
        print(f'The turned to the {direction}')

    def show_speed(self):
        print(f'Car`s speed is {self.speed} km/h')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('You have exceeded the speed!')
        else:
            print(f'Car`s speed is {self.speed} km/h')

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('You have exceeded the speed!')
        else:
            print(f'Car`s speed is {self.speed} km/h')

class PoliceCar(Car):
    pass

class SportCar(Car):
    pass

wc = WorkCar(70, 'blue', 'tractor', False)
wc.go()
wc.turn('left')
wc.show_speed()

pc = PoliceCar(90, 'white', 'jeep', True)
print(pc.is_police)
print(pc.color)

c = Car(50,'red', 'Lada', False)
c.go()
c.stop()
