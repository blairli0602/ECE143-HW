import numpy as np
from matplotlib.pylab import subplots, cm
import matplotlib.pyplot as plt
import random


def gen_rand_slash(m=6, n=6, direction='back'):
    '''
    generate random slash
    :m: int, row
    :n: int, col
    :direction: str: back or forward
    '''

    assert isinstance(m, int)
    assert isinstance(n, int)
    assert m > 1 and n > 1
    assert isinstance(direction,str)
    assert direction in ['back', 'forward']

    resultArray = np.zeros([m, n])
    min_num = min(m, n)

    len = random.randint(2, min_num)
    if direction == 'back':

        start_row = random.randint(1, m - len + 1)  # 3
        start_col = random.randint(1, n - len + 1)  # 2

        for i in range(len):
            resultArray[start_row - 1][start_col - 1] = 1
            start_row += 1
            start_col += 1
    else:
        start_row = random.randint(len, m)
        start_col = random.randint(1, n - len + 1)

        for i in range(len):
            resultArray[start_row - 1][start_col - 1] = 1
            start_row -= 1
            start_col += 1

    return resultArray


fig, axs = subplots(3,3,sharex=True,sharey=True)

for ax in axs.flatten():
    ax.imshow(gen_rand_slash(m=5,n=5,direction='back'),cmap=cm.gray_r)
plt.show()
