import AbstractMethod


class Rectangle(AbstractMethod.AbstractMethod):
    def __calc_right_int(self):
        result = 0
        for i in range(1, self._n + 1):
            result += self._f(self._a + self._h * i) * self._h
        return result

    def __solve_right_int(self):
        self._n = 4
        result_n = self.__calc_right_int()
        self._n *= 2
        self._calc_h()
        result_2n = self.__calc_right_int()
        while abs(result_2n - result_n) > self._eps:
            result_n = result_2n
            self._n *= 2
            self._calc_h()
            result_2n = self.__calc_right_int()
        self._result = result_2n
        self._print_result('Правые прямоугольники')

    def __calc_left_int(self):
        result = 0
        for i in range(self._n):
            result += self._f(self._a + self._h * i) * self._h
        return result

    def __solve_left_int(self):
        self._n = 4
        result_n = self.__calc_left_int()
        self._n *= 2
        self._calc_h()
        result_2n = self.__calc_left_int()
        while abs(result_2n - result_n) > self._eps:
            result_n = result_2n
            self._n *= 2
            self._calc_h()
            result_2n = self.__calc_left_int()
        self._result = result_2n
        self._print_result('Левые прямоугольники')

    def __calc_middle_int(self):
        result = 0
        for i in range(self._n):
            result += self._f(self._a + self._h * (i + 0.5)) * self._h
        return result

    def __solve_middle_int(self):
        self._n = 4
        result_n = self.__calc_middle_int()
        self._n *= 2
        self._calc_h()
        result_2n = self.__calc_middle_int()
        while abs(result_2n - result_n) > self._eps:
            result_n = result_2n
            self._n *= 2
            self._calc_h()
            result_2n = self.__calc_middle_int()
        self._result = result_2n
        self._print_result('Метод средних')

    def solve(self):
        self._calc_h()
        self.__solve_middle_int()
        self.__solve_left_int()
        self.__solve_right_int()
