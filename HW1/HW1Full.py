def is_string_integer(x):
    """
    This function takes a single string character (i.e., 'a','b','c')
    as input and returns True or False if that character
    represents a valid integer in base 10.

    param x:input chart
    type x:str
    returns: int
    """

    assert isinstance(x, str)
    assert len(x) == 1

    if len(x) != 1:
        return False

    if not type(x) is int:
        return False
    else:
        return True


def convert_hex_to_RGB(x):
    """
    This function takes a list of color hex-codes and convert
    them into a list of RGB tuples.

    param x:input list
    type x: list
    returns: list
    """

    assert isinstance(x, list)

    result = []

    for i in range(len(x)):

        assert len(x[i]) == 7
        assert x[i][0] == '#'

        x[i] = x[i].lstrip('#')

        for j in x[i]:
            assert ('0' <= j <= '9') or ('A' <= j <= 'F') or ('a' <= j <= 'f')

        x[i] = tuple(int(x[i][j:j + 2], 16) for j in (0, 2, 4))
        result.append(x[i])

    return result


def compute_average_word_length(instring, unique=False):
    """
    this function calculate the average length of the words in the input string
    unqiue identifier will exclude duplicate words once its set to True
    case sensitive

    param x: input string
    type x: instr
    returns: int
    """
    assert len(instring) >= 0
    assert isinstance(instring,str)

    instring = list(instring.split(" "))
    x1 = []

    sumlen = 0

    if unique is False:

        for i in range(len(instring)):
            sumlen = sumlen + len(instring[i])

        avglen = sumlen / len(instring)

    if unique is True:

        for i in range(len(instring)):
            if instring[i] in x1:
                i += 1
            else:
                x1.append(instring[i])
                #print(x1)
            print (i)

        for i in range(len(x1)):
            sumlen = sumlen + len(x1[i])

        avglen = sumlen / len(x1)

    return avglen


def compute_average_word_length1(instring, unique=False):

    """
    this function calculate the average length of the words in the input string
    unqiue identifier will exclude duplicate words once its set to True
    case sensitive

    param x: input string
    type x: instr
    returns: int
    """
    assert len(instring) != 0
    assert isinstance(instring, str)

    instring = list(instring.split(" "))
    x1 = []

    sumlen = 0

    if unique is False:

        for i in range(len(instring)):
            sumlen = sumlen + len(instring[i])

        avglen = sumlen / len(instring)

    if unique is True:

        for i in range(len(instring)):
            if instring[i] not in x1:
                x1.append(instring[i])

        for i in range(len(x1)):
            sumlen = sumlen + len(x1[i])

        avglen = sumlen / len(x1)

    return avglen

if __name__ == '__main__':

    # result = is_string_integer('a')
    # result = convert_hex_to_RGB(['#B12345', '#FFAABB', '#2319dd'])
    # (177, 35, 69) (255, 170, 187) ()

    result = compute_average_word_length1('''A b ab c''', True)

    print(result)
