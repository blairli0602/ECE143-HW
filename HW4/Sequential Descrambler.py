from itertools import combinations,permutations
from collections import Counter, defaultdict
import copy

def descrambler(w, k):
    """
    :param w: sequence of lower case letters
    :type w:
    :param k: number of words
    :type k:
    :return:
    :rtype:
    """
    assert isinstance(w, str)
    assert isinstance(k, tuple)
    for elem in k:
        assert isinstance(elem, int)

    #f = open('words.txt','r')
    FILENAME = "words.txt"
    #FILENAME = "google-10000-english-no-swears.txt"  #自测
    with open(FILENAME, "r") as f:
        text = f.read()
        words = text.splitlines()

    dictionary = create_dictionary(words)
    dictionary = filter_dictionary(dictionary, w)
    k = list(sorted(k, reverse=False))   #reverse=True降序，False升序
    yield from _recursive_search(w, dictionary, k)


def create_dictionary(words):
    d = defaultdict(list)
    for word in words:
        key = "".join(sorted(word))
        d[key].append(word)

    return d


def filter_dictionary(dictionary, word):
    d = defaultdict(list)
    for k, v in dictionary.items():
        foreign = False
        for char in k:
            if char not in word:
                foreign = True
                break
        if not foreign:
            d[k] = v
    return d


def word_count(word):
    return tuple(Counter(word).most_common())

def word_from_count(word_count):
    return "".join([v[1]*v[0] for v in word_count])


def count_difference(count1, count2):
    d1 = dict(count1)
    d2 = dict(count2)

    d3 = copy.deepcopy(d1)
    for k, v in d2.items():
        diff = d1[k] - d2[k]
        if diff > 0:
            d3[k] = diff
        else:
            d3.pop(k)

    return tuple(Counter(d3).most_common())


def _recursive_search(w, dictionary, k, existing=None):
    """
    finds the substrings
    :param w:
    :type w:
    :param counts:
    :type counts:
    :param k:
    :type k:
    :param existing:
    :type existing:
    :return:
    :rtype:
    """

    if existing is None:
        existing = list()

    if len(k) == 0:
        yield " ".join(existing)
    else:
        substrs = list(combinations(w, r=k[0]))
        substrs = {"".join(sorted(substr)) for substr in substrs}

        for substr in substrs:
            for word in dictionary[substr]:
                n_existing = copy.deepcopy(existing)
                n_existing.append(word)
                n_w = word_from_count(count_difference(word_count(w), word_count(substr)))
                n_k = copy.deepcopy(k)
                n_k.pop(0)
                yield from _recursive_search(n_w, dictionary, n_k, existing=n_existing)


# def selfit(words,num):
#     list = []
#     for i in itertools.permutations(words,num[1]):
#         if i in map:
#             words = words - i   #原words里面减少这些字母
#             num = num[1:]       #num切掉第一个元素
#             if len(num) == 0:
#                 list.append(i)
#                 return list
#             next = selfit(words,num[1])
#             return itertools.product(i,next)

#自测
# if __name__ == '__main__':
#print(list(descrambler("hime", (2,2))))
# print(list(descrambler("choeounokeoitg", (3,5,6))))
#print(list(descrambler('qeodwnsciseuesincereins', (4, 7, 12))))
#     print(list(descrambler(w = 'trleeohelh' , k=(5,5))))

print(word_count('hime'))
print(word_from_count(count_difference(word_count('himee'),word_count('me'))))