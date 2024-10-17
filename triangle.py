def area(a, h):
    """
    Параметры:
        a - вещественное число, одна сторона треугольника
        h - вещественное число, высота треугольника, проведенная к стороне (a)
    Возвращаемое значение:
        вещественное число, площадь треугольника с заданными сторонами (a, h)
    """
    return a * h / 2

def perimeter(a, b, c):
    """
    Параметры:
        a - вещественное число, первая сторона треугольника
        b - вещественное число, вторая сторона треугольника
        c - вещественное число, третья сторона треугольника
    Возвращаемое значение:
        вещественное число, периметр треугольника с заданными сторонами (a, b, c)
    """
    return a + b + c