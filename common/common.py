import math
def linear_space(start, stop, num):
    step = (stop - start) / (num - 1)
    return [start + i * step for i in range(num)]

def chebyshev_space(start, stop, num):
    return [0.5 * (start + stop) + 0.5 \
            * (stop - start) * math.cos(math.pi * (2 * i + 1) / (2 * num)) for i in range(num)]

def calculate_mse(original_y, interpolated_y):
    mse = 0
    n = len(original_y)
    for i in range(n):
        mse += (original_y[i] - interpolated_y[i]) ** 2
    mse /= n
    return mse