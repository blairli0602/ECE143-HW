import random

def get_sample(nbits=3,prob=None,n=1):
    """
    break a list of words into chunks of five

    param words: input list of string words
    param fname: input list of string words
    type x: int
    returns: list

    """

    val = list(prob.keys())
    pr = list(prob.values())

    assert isinstance(prob,dict)
    for items in val:
        assert len(items) == nbits
        for j in items:
            assert j == '0' or j == '1'

    for k in pr:
        assert 0 <= k <= 1

    assert sum(pr) == 1

    result = [random.choices(val,pr)[0] for i in range(n)]

    return result


#p = {'000': 0.125,'001': 0.125,'010': 0.125, '011': 0.125, '100': 0.125, '101': 0.125,'110': 0.125,'111': 0.125}

p = {"10": 0.99, "11": 0.01}

x = get_sample(2,p,3)
print(x)