import AbstractMethod


class Trapezoid(AbstractMethod.AbstractMethod):
    def __calc_int(self):
        result = 0
        for i in range(self._n):
            result += (self._f(self._a + self._h * i) + self._f(self._a + self._h * (i + 1))) / 2 * self._h
        return result

    def __solve_int(self):
        self._calc_h()
        result_h = self.__calc_int()
        self._n *= 2
        self._calc_h()
        result_2h = self.__calc_int()
        while abs(result_2h - result_h) > self._eps:
            result_h = result_2h
            self._n *= 2
            self._calc_h()
            result_2h = self.__calc_int()
        self._result = result_2h
        self._print_result('Метод трапеций')

    def solve(self):
        self.__solve_int()
