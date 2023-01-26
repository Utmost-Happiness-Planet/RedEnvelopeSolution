from RedEnvelopeSolution import RedEnvelopeSolution, plt_show, set_plt_backend
from RedEnvelopeSolution.red import adjust

# 上下浮动倍率，其中一个为0则不进行调整
floating_max = 2
floating_min = 10

# 记得修改backend
set_plt_backend('qtagg')

red_envelope_1 = RedEnvelopeSolution(55, 100)
print(f'str {red_envelope_1}')
print(f'getitem {red_envelope_1[0]}')

red_envelope_2 = RedEnvelopeSolution(55,
                                     100,
                                     show=True,
                                     floating=(floating_max, floating_min),
                                     adjust_func=adjust)
plt_show()
