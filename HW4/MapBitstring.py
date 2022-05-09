
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


x = ['100', '100', '110', '010', '111', '000', '110', '010', '011', '000']
y = map_bitstring(x)
print(y)