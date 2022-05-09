import copy
import itertools
from collections import Counter, defaultdict

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
        for j in y.keys():
            new_i = ''.join(new_i)
            if new_i == j:
                for k in y[j]:
                    finalString.append(''.join(k))

    finalString = set(finalString)

    return finalString


def get_word_set(w):
    """
    takes a
    param x: input list
    returns: dict
    """
    f = open("/tmp/google-10000-english-no-swears.txt", 'r')
    lines = list(f.read().splitlines())
    mapwords = defaultdict(list)

    for k in lines:
        key = "".join(sorted(k))
        mapwords[key].append(k)

    mapwords_new = defaultdict(list)

    for k, v in mapwords.items():
        foreign = False
        for char in k:
            if char not in w:
                foreign = True
                break
        if not foreign:
            mapwords_new[k] = v

    return mapwords_new


def remove_words(string, words):
    """
    takes a
    param x: input list
    returns: dict
    """
    for p in words:
        string = string.replace(p, '', 1)
    return string


def recurisve(w, k, prev, int, final):
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
        if len(prev.replace(" ", "")) == int:
            final.append(answer)
        return

    new_k = copy.deepcopy(k)
    new_ki = k[0]

    new_k.pop(0)
    word_set = get_word_set(w)

    word_substring = get_substring(w, new_ki, word_set)
    for j in word_substring:
        new_w = remove_words(w, j)
        recurisve(new_w, new_k, prev + ' ' + j, int, final)


def descrambler(w, k):
    """
    takes a
    param x: input list
    returns: dict
    """
    assert isinstance(w, str)
    for char in w:
        assert ('a' <= char <= 'z')
    assert isinstance(k, tuple)
    for j in k:
        assert isinstance(j, int)

    final = []
    finalresult = []
    recurisve(w, k, '', len(w), final)
    for i in final:
        i = i.lstrip()
        finalresult.append(i)

    return finalresult


# print(list(descrambler("hime", (2,2))))
# print(list(descrambler("choeounokeoitg", (3,5,6))))
print(list(descrambler('qeodwnsciseuesincereins', (4, 7, 12))))

#print(descrambler('trleeohelh', (5, 5)))

#print(get_word_set('trleeohelh'))