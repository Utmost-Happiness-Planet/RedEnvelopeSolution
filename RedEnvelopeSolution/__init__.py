import random
from typing import Callable, Optional

import matplotlib
import matplotlib.pyplot as plt


class RedEnvelopeSolution:

    def __init__(
            self,
            num: int,
            money: float,
            # 一块钱最多分为多少份，支持小数
            least_money: float = 100,
            *_,
            show: bool = False,
            alpha: Optional[float] = None,
            floating: Optional[tuple[float, float]] = None,
            generate_func: Optional[Callable[['RedEnvelopeSolution'], tuple[list[int],
                                                                            list[int]]]] = None,
            adjust_func: Optional[Callable[['RedEnvelopeSolution'], list[int]]] = None) -> None:
        self.n = num
        self.m = money
        # 一块钱最多分为多少份，支持小数
        self.lni1 = least_money

        self.generate_data: Callable[[], tuple[list[int], list[int]]]
        if generate_func is None:
            self.generate_data = default_generate_data
        else:
            self.generate_data = generate_func
        self.data: list[int]
        self.origin: list[int]
        self.data, self.origin = self.generate_data(self)
        if show:
            self.print(1)

        if alpha is not None or floating is not None:
            if floating is not None:
                # 上下浮动倍率，其中一个为0则不进行调整
                self.f_max = floating[0]
                self.f_min = floating[1]
            if alpha is not None:
                self.alpha = alpha
            self.adjust_data: Callable[[], list[int]]
            if adjust_func is None:
                self.adjust_data = default_adjust_data
            else:
                self.adjust_data = adjust_func
            self.data = self.adjust_data(self)
            if show:
                self.print(2)
        if show:
            plt.show()

    def __str__(self) -> str:
        return str([d / self.lni1 for d in self.data])

    def __getitem__(self, index: int) -> float:
        return self.data[index] / self.lni1

    def print(self, i):
        float_data = [d / self.lni1 for d in self.data]
        print(f'float data: {float_data}')
        print(f'sum: {sum(float_data)}')
        plt.scatter(range(0, self.n), float_data, marker=f'{i}')


def default_generate_data(self:RedEnvelopeSolution) -> tuple[list[int], list[int]]:
    m = int(self.m * self.lni1)
    try:
        l = random.sample(range(1, m), self.n - 1)
    except Exception:
        print('money not enough')
        return []
    l.extend([0, m])
    l.sort()
    return [l[i + 1] - l[i] for i in range(self.n)], l

def default_adjust_data(self:RedEnvelopeSolution) -> list[int]:
    return self.data

def set_plt_backend(s: str):
    matplotlib.use(s)
