
import itertools

def get_power_of3(x):

    """
    construct any number between 1 and 40

    param x: input int
    type x: int
    returns: list
    """
    assert 0 <= x <= 40
    assert isinstance(x, int)

    coe = [-1, 0, 1]
    per = list(itertools.product(coe, repeat=4))
    wei = [1,3,9,27]
    input = []
    out = []

    for i in range(len(per)):
        result = 0

        for j in range(4):
            result = result + (per[i][j] * wei[j])

        combin1 = list(per[i])
        input.append(str(result))
        out.append(combin1)

    res = {input[k]: out[k] for k in range(len(input))}

    x = str(x)
    z = res.get(x)

    return z

def write_chunks_of_five(words ,fname):

    """
    break a list of words into chunks of five

    param words: input list of string words
    param fname: input list of string words
    type x: int
    returns: list

    """
    assert len(words) > 0
    assert isinstance(words, list)
    for i in range(len(words)):
        for j in words[i]:
            assert ('A' <= j <= 'Z') or ('a' <= j <= 'z')

    l = len(words)
    q = l // 5
    newlen = q * 5

    f = open(fname, 'w')

    for i in range(l):
        i = i + 1
        if i % 5 != 0:
            f.write(str(words[i-1]) + ' ')
        elif i % 5 == 0:
            f.write(str(words[i-1]) + '\n')

    f.close()
    return f

def write_columns(data,fname):

    """
    break a list of words into chunks of five

    param words: input list of numbers can be int or float
    param fname: input list of string for file name
    returns: file with file name fname

    """
    assert len(data) > 0
    for i in data:
        assert type(i) == int or type(i) == float


    f = open(fname, 'w')

    for i in data:
        f.write(str(i) + ',' + str(i**2) + ',' + str( round((i+i**2)/3,2 ) )  + '\n')

    f.close()
    return f

if __name__ == '__main__':

    result = get_power_of3(3)

    print(result)

    coe = [-1,0,1]
    l1 = list(itertools.combinations_with_replacement(coe, 4))

    data=[5,4,6,1,9,0,3,9,2,7,10,8,4,7,1,2,7,6,5,2,8,2,0,1,1,1,2,10,6,21.5]

    result = write_columns(data, 'test')

    print(result)