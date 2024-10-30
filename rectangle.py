from utils import correct_value


def area(a, b) -> float:
    """
    Параметры:
        a - вещественное число, одна сторона прямоугольника
        b - вещественное число, другая сторона прямоугольника
    Возвращаемое значение:
        вещественное число, площадь прямоугольника с заданными сторонами (a, b)
    """
    if not (correct_value(a) and correct_value(b)):
        return 0
    return a * b


def perimeter(a, b) -> float:
    """
    Параметры:
        a - вещественное число, одна сторона прямоугольника
        b - вещественное число, другая сторона прямоугольника
    Возвращаемое значение:
        вещественное число, периметр прямоугольника с заданными сторонами (a, b)
    """
    if not (correct_value(a) and correct_value(b)):
        return 0
    return (a + b) * 2 * correct_value(a) * correct_value(b)