import math


class Vmixin:
    def get_area(self):
        result = 0
        for side in self.figure:
            result += side.get_area(self)
        return result


class Square:
    def __init__(self, length):
        self.side_length = length

    @property
    def side_length(self):
        return self._side_length

    @side_length.setter
    def side_length(self, length):
        self._side_length = length

    def get_perimeter(self):
        return self.side_length * 4

    def get_area(self):
        return self._side_length ** 2


class Cube(Square, Vmixin):
    def __init__(self, length):
        super().__init__(length)
        self.square = Square
        self.figure = [self.square for _ in range(6)]


class Triangle:
    def __init__(self, length, height):
        self.side_length = length
        self.height = height

    @property
    def side_length(self):
        return self._side_length

    @side_length.setter
    def side_length(self, length):
        self._side_length = length

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    def get_area(self):
        return self.side_length / 2 * self.height

    def get_perimeter(self):
        edge_triangle = math.sqrt(self.height ** 2 + (self.side_length / 2) ** 2)
        return round(self.side_length + 2 * edge_triangle, 3)


class Pyramid(Triangle, Square, Vmixin):
    def __init__(self, length, height):
        super().__init__(length, height)
        self.square = Square
        self.triangle = Triangle
        self.figure = [self.square]
        self.figure.extend([self.triangle for _ in range(4)])


print(f'---Квадрат')
a = Square(10)
print(f'Периметр квадрата со стороной {a.side_length}: {a.get_perimeter()}')
print(f'Площадь квадрата со стороной {a.side_length}: {a.get_area()}')
print(f'---Куб')
c = Cube(8)
print(f'Площадь граней куба с длиной стороны {c.side_length}: {c.get_area()}')

print(f'---Треугольник')
t = Triangle(10, 10)
print(f'Периметр треугольника с основанием {t.side_length} и высотой {t.height}: {t.get_perimeter()}')
print(f'Площадь треугольника со стороной {t.side_length}: {t.get_area()}')

print('---Пирамида')
p = Pyramid(5, 7)
print(f'Площадь ганей пирамиды с длиной основания {p.side_length} и высотой грани {p.height}: {p.get_area()}')