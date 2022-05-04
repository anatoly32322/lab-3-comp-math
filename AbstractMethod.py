class AbstractMethod:
    _n: int = 4
    _f = None
    _h: float
    _a: float
    _b: float
    _result: float
    _eps: float

    def __init__(self, f, a, b, eps):
        self._f = f
        self._a = a
        self._b = b
        self._eps = eps

    def _calc_h(self):
        self._h = (self._b - self._a) / self._n

    def _print_result(self, method):
        print('Результат вычисления интеграла методом "{method}" равен {result}'
              .format(method=method, result=self._result))
        print('n = {}'.format(self._n))
