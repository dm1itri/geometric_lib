import math
from utils import correct_value


def area(r) -> float:
    """
    Параметры:
        r - вещественное число, радиус круга
    Возвращаемое значение:
        вещественное число, площадь круга с заданным радиусом (r)
    """
    if not correct_value(r):
        return 0
    return r * r * math.pi


def perimeter(r) -> float:
    """
    Параметры:
        r - вещественное число, радиус круга
    Возвращаемое значение:
        вещественное число, периметр круга с заданным радиусом (r)
    """
    if not correct_value(r):
        return 0
    return 2 * math.pi * r

