import math

class Figure:
    def __init__(self, color, sides, filled=False):
        self.__sides = sides             # Приватный атрибут
        self.__color = list(color)
        self.filled = filled             # Публичный атрибут
        self.sides_count = len(sides)    # Количество сторон

    def __is_valid_color(self, r, g, b):
        return all(0 <= x <= 255 for x in (r, g, b))

    def get_color(self):
        return self.__color

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        return all(isinstance(side, int) and side > 0 for side in new_sides) and len(new_sides) == self.sides_count

    def get_sides(self):
        return self.__sides                # Доступ к приватному атрибуту

    def __len__(self):
        return sum(self.__sides)           # Периметр фигуры

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)  # Изменяем приватный атрибут

class Circle(Figure):
    def __init__(self, color, radius, filled=False):
        sides = [1]  # Круг имеет одну сторону
        super().__init__(color, sides, filled)
        self.__radius = radius

    def get_square(self):
        return math.pi * (self.__radius ** 2)  # Площадь круга

    def set_sides(self, *new_sides):
        super().set_sides(*new_sides)
        if self.get_sides():
            self.__radius = self.get_sides()[0] / (2 * math.pi)

class Triangle(Figure):
    def __init__(self, color, a, b, c, filled=False):
        sides = [a, b, c]
        super().__init__(color, sides, filled)

    def get_square(self):
        # Используем формулу Герона для расчета площади
        a, b, c = self.get_sides()        # Доступ к приватному атрибуту
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

class Cube(Figure):
    def __init__(self, color, side_length, filled=False):
        sides = [side_length] * 12  # 12 одинаковых сторон
        super().__init__(color, sides, filled)

    def get_volume(self):
        sides_count = self.get_sides()
        return sides_count[0] ** 3 if sides_count else 0  # Объем куба (приватный атрибут)

# Примеры использования:
circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
