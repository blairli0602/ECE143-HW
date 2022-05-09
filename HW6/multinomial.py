import random

def multinomial_sample(n, p, k=1):
    '''
    Return samples from a multinomial distribution.

    n:= number of trials
    p:= list of probabilities
    k:= number of desired samples
    multinomial_sample(10,[1/3,1/3,1/3],k=10)
     [[3, 3, 4],
      [4, 4, 2],
      [3, 4, 3],
      [5, 2, 3],
      [3, 3, 4],
      [3, 4, 3],
      [6, 2, 2],
      [2, 6, 2],
      [5, 4, 1],
      [4, 4, 2]]
    '''

    assert isinstance(n, int)
    assert n > 0
    for item in p:
        assert isinstance(item,int) or isinstance(item,float)
    assert isinstance(p, list)
    assert sum(p) == 1
    assert k >= 1
    assert isinstance(k, int)


    population = list(range(len(p)))
    weights = p

    result = []

    for p in range(k):
        dic = {}
        trail = []
        for i in population:
            dic[i] = None

        for j in range(n):
            cho = random.choices(population,weights)
            trail.append(cho[0])

        for keys in dic.keys():
            dic[keys] = trail.count(keys)

        result.append(list(dic.values()))

    return result

n = 2
p = [0.5,0,0.5, 0]
k = 3
print(multinomial_sample(n, p, k))
