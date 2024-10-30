from utils import correct_value


def area(a) -> float:
    """
    Параметры:
        a - вещественное число, сторона квадрата
    Возвращаемое значение:
        вещественное число, площадь прямоугольника с заданными сторонами (a)
    """
    if not (correct_value(a)):
        return 0
    return a * a * correct_value(a)


def perimeter(a) -> float:
    """
    Параметры:
        a - вещественное число, сторона квадрата
    Возвращаемое значение:
        вещественное число, периметр прямоугольника с заданными сторонами (a)
    """
    if not (correct_value(a)):
        return 0
    return 4 * a * correct_value(a)
