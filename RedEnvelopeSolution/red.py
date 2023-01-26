from RedEnvelopeSolution import RedEnvelopeSolution


def adjust(self: RedEnvelopeSolution):
    avg = self.m / self.n * self.lni1
    float_range = (int(avg * self.f_max), int(avg / self.f_min))
    float_value = float_range[0] + float_range[1]
    avg = int(avg)
    # 超出浮动范围
    over = []
    under = []
    # 平均值上下，用于微调
    sm_over = []
    sm_under = []
    for i in range(self.n):
        v = self.origin[i + 1] - self.origin[i]
        if v > float_range[0]:
            over.append(i)
        elif v <= float_range[1]:
            under.append(i)
        elif v > avg:
            sm_over.append(i)
        elif v <= avg:
            sm_under.append(i)
    o_len = len(over)
    u_len = len(under)
    # 大于浮动范围的和小于浮动范围的调整至范围边界
    temp = 0
    for i in range(min(o_len, u_len)):
        o_v = self.data[over[i]]
        u_v = self.data[under[i]]
        temp = temp + o_v + u_v - float_value
        self.data[over[i]] = float_range[0]
        self.data[under[i]] = float_range[1]
    # 大于小于浮动范围的长度不相等部分
    if o_len > u_len:
        for i in range(u_len, o_len):
            o_v = self.data[over[i]]
            temp = temp + o_v - float_range[0]
            self.data[over[i]] = float_range[0]
    elif o_len < u_len:
        for i in range(o_len, u_len):
            u_v = self.data[under[i]]
            temp = temp + u_v - float_range[1]
            self.data[under[i]] = float_range[1]

    # 微调，用来处理浮动范围调整完以后temp中剩余的部分
    def sm_adjust(sm_list, length, temp, f):
        add = int(temp / length)
        if add == 0:
            for i in range(temp):
                self.data[sm_list[i]] = self.data[sm_list[i]] + f
        else:
            for i in range(length):
                self.data[sm_list[i]] = self.data[sm_list[i]] + add
            temp = temp - add * length
            if temp is not 0:
                self.data[sm_list[-1]] = self.data[sm_list[-1]] + temp

    sm_under_len = len(sm_under)
    sm_over_len = len(sm_over)
    if temp > 0:
        if sm_under_len > 0:
            sm_adjust(sm_under, sm_under_len, temp, 1)
        else:
            sm_adjust(sm_over, sm_over_len, temp, 1)
    elif temp < 0:
        if sm_over_len > 0:
            sm_adjust(sm_over, sm_over_len, temp, -1)
        else:
            sm_adjust(sm_under, sm_under_len, temp, -1)
    return self.data
