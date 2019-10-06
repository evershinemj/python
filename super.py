# class Coffee is defined in module withas.py
from withas import Coffee


class Latte(Coffee):
    def __init__(self):
        super().__init__('Latte')

    def __str__(self):
        pass
        return super().__str__()

    def __repr__(self):
        pass
        super().__repr__()

    def __format__(self):
        pass

    def __enter__(self):
        pass
        super().__enter__()

    # def __exit__(self):
    def __exit__(self, exc_tp, exc_val, traceback):
        pass
        super().__exit__(exc_tp, exc_val, traceback)


if __name__ == '__main__':
    latte = Latte()
    with latte as l:
        print('Drinking ' + str(latte))
