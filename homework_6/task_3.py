# 3) Реализовать базовый класс ​ Worker ​ (работник), в котором определить
# атрибуты: name, surname , position(должность),income(доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus}. Создать класс ​ Position ​ (должность)
# на базе класса ​Worker​.В классе Position реализовать методы получения
# полного имени сотрудника (get_full_name)и дохода с учетом премии
# (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса ​Position, передать данные, проверить значения атрибутов,
# вызвать методы экземпляров).

class Worker:
    def __init__(self, n, s, p, w, b):
        self.name = n
        self.surname = s
        self.position = p
        self._income = {"wage": w, "bonus": b}

class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        result = sum(self._income.values())
        print(f'Total income of {self.name} {self.surname} - {result}')

p = Position('Ivan', 'Ivanov', 'lawer', 120000, 79000)
print(p.name)
print(p.surname)
print(p.position)
print(p._income)
p.get_full_name()
p.get_total_income()






