
def slide_window1(x,width,increment) :

    """
    break a list of words into chunks of five

    param words: input list of numbers can be int or float
    param fname: input list of string for file name
    returns: file with file name fname

    """
    assert isinstance(increment,int)
    assert isinstance(width,int)
    assert isinstance(x,list)

    assert increment > 0
    assert width > 0

    result  = []
    print(x)
    for i in range(len(x) - width + 1):
        if i == 0:
            result.append(list(x[i:i+width]))
        else:
            result.append(list())


    return result

def slide(x,width,increment):
    for i in range(len(x) - width + 1):
        if i == 0:
            yield x[i:i + width]
        if i + increment + width > len(x):
            return
        else:
            yield i + 1
                #x[i + increment: i + increment + width]

def foo(x,width,increment):
    for i in range(len(x) - width + 1):
        if i == 0:
            yield x[i:i+width]
        elif i + increment + width > len(x):
            return
        else:
            i = i + increment
            yield x[i: i + width]


def slide_window(x,width,increment) :

    """
    Implement a sliding window for an arbitrary input list.

    param x: input list of integer
    param width: size of the window
    param increment: size between each step
    returns: list of full sub list of numbers

    """
    assert isinstance(increment,int)
    assert isinstance(width,int)
    assert isinstance(x,list)

    assert increment > 0
    assert width > 0
    result = []

    for i in range(0,len(x),increment):

        if i + width > len(x):
            return result
        else:
            result.append(x[i: i + width])

    return result


if __name__ == '__main__':

    result = slide_window(list(range(18)),5,2)

    print(result)