import copy
import itertools

def get_substring(w, x, y):
    """
    takes a
    param x: input list
    returns: dict
    """
    string = list(itertools.combinations(w, x))
    finalString = []
    for i in string:
        new_i = sorted(i)
        for j in y :
            new_j = sorted(j)
            if new_i == new_j:
                finalString.append(''.join(j))

    finalString = set(finalString)

    return finalString

def get_word_set():
    """
    takes a
    param x: input list
    returns: dict
    """
    f = open('words.txt','r')
    lines = list(f.read().splitlines())
    mapwords = set()

    for k in lines:
         mapwords.add(k)

    return mapwords

def remove_words(string, words):
    """
    takes a
    param x: input list
    returns: dict
    """
    for p in words:
        string = string.replace(p, '', 1)
    return string

def recurisve(w, k, prev, int,final):
    """
    takes a
    param x: input list
    param k: input list
    param prev: input list
    param int: input list
    param final: input list
    returns: dict
    """
    k = list(k)
    if len(k) == 0:
        answer = prev
        if len(prev.replace(" ","")) == int:
            yield answer.lstrip()
    else:
        new_k = copy.deepcopy(k)
        new_ki = k[0]

        new_k.pop(0)
        word_set = get_word_set()

        word_substring = get_substring(w, new_ki, word_set)

        for j in word_substring:
            new_w = remove_words(w,j)
            yield from list(recurisve(new_w,new_k,prev + ' ' + j, int, final))

def descrambler(w,k):
    """
    takes a
    param x: input list
    returns: dict
    """
    assert isinstance(w, str)
    for char in w:
        assert ('a' <= char <= 'z')
    assert isinstance(k,tuple)
    for j in k:
        assert isinstance(j, int)

    final = list()
    yield from list(recurisve(w, k, '', len(w), final))

#print(list(descrambler("hime", (2,2))))
#print(list(descrambler("choeounokeoitg", (3,5,6))))
#print(list(descrambler('qeodwnsciseuesincereins', (4, 7, 12))))

print(list(descrambler(w = 'trleeohelh' , k=(5,5))))
