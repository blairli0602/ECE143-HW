import random
import collections
import typing as tp

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

def map_bitstring(x):
    """
    takes a list of bitstrings (i.e., 0101) and maps each bitstring to 0 if the number of 0s in the bitstring strictly exceeds the number of 1s. Otherwise, map that bitstring to 1.

    param x: input list
    returns: dict
    """

    assert isinstance(x,list)
    assert len(x) > 0
    for items in x:
        for j in items:
            assert j == '0' or j == '1'

    out = []
    for i in x:
        zero = i.count('0')
        one = i.count('1')

        if zero > one:
            out.append(0)
        else:
            out.append(1)

    result = dict(zip(x,out))
    return result

def gather_values(x):
    """
    generate n samples and tally the number of times an existing key is repeated.
    Generate a new dictionary with bitstrings as keys and with values as lists that contain the corresponding mapped values from map_bitstring.

    param x: input list
    returns: dict
    """

    assert isinstance(x,list)
    assert len(x) > 0

    keys = set(x)
    times = []
    for i in keys:
        times.append(x.count(i))

    TimesBit = []
    keys = list(keys)

    x = map_bitstring(keys)
    mapx = list(x.values())

    #print(times, keys, mapx)

    for j in range(len(times)):
         TimesBit.append([mapx[j] for k in range(times[j])])

    result = dict(zip(keys,TimesBit))
    return result

def threshold_values(seq,threshold = 1):
    """
    param x: sequence received from get sample
    returns: dict
    """
    assert isinstance(seq, list)
    assert len(seq) > 0
    assert isinstance(threshold, int)

    newseq = gather_values(seq)

    newseq1 = {}
    for i in newseq.keys():
       if newseq[i][0] == 1:
            newseq1[i] = len(newseq[i])
    key = []
    for j in range(threshold):
        maxi = max(newseq1, key=newseq1.get)
        key.append(maxi)
        del newseq1[maxi]

    for i in newseq.keys():
        if i in key:
            newseq[i] = 1
        else:
            newseq[i] = 0

    return newseq



#x = ['10', '11', '01', '00', '10', '00', '00', '11', '10', '00', '00', '01', '01', '11', '10', '00', '11', '10', '11', '11']

x= ['1111', '0110', '1001', '0011', '0111', '0100', '0111', '1100', '0011', '0010', '0010', '1010', '1010', '1100', '0110', '0101', '0110', '1111', '1001', '0110', '0010', '1101', '0101', '0010', '0100', '0010', '0000', '0000', '0011', '0110', '0101', '1010', '1011', '1101', '1100', '0111', '1110', '0100', '0110', '1101', '0001', '1110', '0010', '0001', '1010', '1010', '0011', '1000', '0010', '0000', '1010', '1101', '1111', '1000', '1000', '0010', '1010', '0101', '0101', '1101', '0110', '1001', '1100', '1100', '1000', '1010', '0011', '0101', '0101', '0011', '0001', '1010', '0011', '0011', '1101', '1010', '0101', '0011', '1011', '0101', '0000', '1111', '1001', '0101', '1100', '0011', '1111', '1101', '0001', '1111', '1110', '1111', '0001', '0010', '0110', '0100', '0101', '1100', '1110', '1001']
z = threshold_values(x,threshold=8)
print(z)
# x=get_sample(nbits=2,prob=p,n=20)
# print(x)
# y = gather_values(x)
# print(y)
# z = threshold_values(y,threshold=3)
# print(z)