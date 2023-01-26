from RedEnvelopeSolution import RedEnvelopeSolution, set_plt_backend
from RedEnvelopeSolution.red import adjust

# 上下浮动倍率，其中一个为0则不进行调整
floating_max = 2
floating_min = 10

# 记得修改backend
set_plt_backend('qtagg')

# 至少两个参数，即不进行调整
red_envelope_1 = RedEnvelopeSolution(55, 100)
# 获取结果的方式
print(f'str {red_envelope_1}')
print(f'list {red_envelope_1.data}')
print(f'getitem {red_envelope_1[0]}\n===================')

# 调整+显示对比的例子
red_envelope_2 = RedEnvelopeSolution(100,
                                     10000,
                                     show=True,
                                     floating=(floating_max, floating_min),
                                     adjust_func=adjust)
