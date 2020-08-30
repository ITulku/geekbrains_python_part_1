# 2) Реализовать класс ​ Road ​ (дорога), в котором определить
# атрибуты: ​ length ​ (длина), width (ширина). Значения данных атрибутов
# должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия
# одного кв метра дороги асфальтом, толщиной в
# 1 см * число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т

class Road:
    def __init__(self, l, w):
        self._lenght = l
        self._width = w

    def asph_mass(self, mass_of_asphalt,asphalt_thickness ):
        result = (self._lenght * self._width * mass_of_asphalt * asphalt_thickness) / 1000
        print(f'Total mass of asphalt is {result} t.')

r = Road(20, 5000)
r.asph_mass(25,5)



