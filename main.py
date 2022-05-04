from RectangleMethod import Rectangle
from TrapezoidMethod import Trapezoid


def get_func(which_func):
    if which_func == 1:
        return lambda x: -pow(x, 3) - pow(x, 2) - 2 * x + 1
    elif which_func == 2:
        return lambda x: 3 * pow(x, 3) + 5 * pow(x, 2) + 3 * x - 6
    elif which_func == 3:
        return lambda x: -pow(x, 3) - pow(x, 2) + x + 3


if __name__ == '__main__':
    print('Выберете, какую функцию будем интегрировать:')
    print('1) -x^3 - x^2 - 2x + 1')
    print('2) 3x^3 + 5x^2 + 3x - 6')
    print('3) -x^3 - x^2 + x + 3')
    which_func = int(input())
    func = get_func(which_func)
    a, b = map(float, input('Введите границы интегрирования для заданной функции\n').split())
    eps = float(input('Введите погрешность вычисления интеграла\n'))
    rectangle_solver = Rectangle(func, a, b, eps)
    rectangle_solver.solve()
    trapezoid_solver = Trapezoid(func, a, b, eps)
    trapezoid_solver.solve()
