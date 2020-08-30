# 5) Реализовать класс ​ Stationery ​ (канцелярская принадлежность).
# Определить в нем атрибут ​title(название) и метод ​ draw ​ (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса ​ Pen (ручка),Pencil(карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода ​ draw​ .
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('_' * 10)

class Pencil(Stationery):
    def draw(self):
        print('.' * 10)

class Handle(Stationery):
    def draw(self):
        print('*' * 10)

h = Handle('marker')
print(h.title)
h.draw()

pc = Pencil('pencil')
print(pc.title)
pc.draw()

p = Pen('pen')
print(p.title)
p.draw()