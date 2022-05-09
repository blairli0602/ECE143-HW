def compute_average_word_length(instring, unique=False):
    """

    :param instring:
    :param unique:
    :return:
    """
    assert  isinstance(instring,str)
    assert  len(instring) != 0

    if unique == False:
        sum = 0
        string = instring.split(" ")
        for i in string:
            number = len(i)
            sum = sum + number
        average = sum/len(string)
        return average

    if unique == True:
        sum = 0
        string = instring.split(" ")
        list = []
        for i in string:
            list.append(i)
            set1 = set(list)
            #print(set1)
        for j in set1:
            number = len(j)
            #print(number)
            sum = sum + number
            #print(sum)
        average = sum/len(set1)
        return average

if __name__ == '__main__':
    # result = convert_hex_to_RGB(['#B12345', '#FFAABB', '#2319dd'])
    # (177, 35, 69) (255, 170, 187) ()

    result = compute_average_word_length('''a abc''', True)

    print(result)