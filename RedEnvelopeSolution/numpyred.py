import random

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('qtagg')
import numpy as np

tot_number = 20
tot_money = 10
least_number_in_1 = 100


def use_random(n, m):
    m = int(m * least_number_in_1)
    l = random.sample(range(1, m), n - 1)
    l.extend([0, m])
    l.sort()
    return [(l[i + 1] - l[i]) / least_number_in_1 for i in range(n)]


def uniform(n, m):
    if m == 0:
        return [0] * n
    m = int(m * least_number_in_1)
    l = np.array([np.floor(m / n)] * n)
    l[:int(m - l.sum())] += 1
    return l / least_number_in_1


ret = np.array(use_random(tot_number, tot_money))

alpha = 0.5  # 方差调节参数，取值0~1，取值为1时不做调整，随着数值减小方差先减小后增大，在0.5左右达到方差最小值

a = ret.copy()
median = np.median(a)  # 求中位数
# origin_var = a.var()  # 记录原始方差
left_idx = np.where(a < median)[0]
right_idx = np.where(a > median)[0]
right_old = a[right_idx].copy()
a[right_idx] = np.round(a[right_idx] * alpha, 2)
diff = np.round((right_old - a[right_idx]).sum(), 2)
a[left_idx] += np.array(uniform(a[left_idx].size, diff))

print(a)
print(sum(a))
x = np.arange(0, tot_number, 1)
plt.title(f"alpha={alpha} var={a.var()}")
# plt.ylim(-0.1, 0.3)
plt.scatter(x, a)
plt.show()
