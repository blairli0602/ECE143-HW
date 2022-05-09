
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

    data=[5,4,6,1,9,0,3,9,2,7,10,8,4,7,1,2,7,6,5,2,8,2,0,1,1,1,2,10,6,21.5]

    result = write_columns(data, 'test')

    print(result)
