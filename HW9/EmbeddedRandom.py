import random
import itertools as it

def est_prob(n:int, m:int, niter:int=100)->float:
    '''
    :param n: num sides in regular polygon (n>=4)
    :type n: int
    :param m: num vertices for inscribed polygon (m>=3)
    :type m: int
    :param niter: num iterations for simulation
    :type m: int
    '''

    assert isinstance(n,int)

    count = 0
    for i in range(niter):
        com = random.choices(range(n),k=m)
        if len(set(com)) == len(com):
            count += 1

    return float(count/niter)


print(est_prob(10,3,100))

