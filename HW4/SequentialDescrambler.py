import itertools
from collections import Counter, defaultdict
from copy import deepcopy

def get_word_map():
    f = open('words.txt','r')
    lines = list(f.read().splitlines())
    mapwords = {}

    for k in range(len(lines)):
         mapwords[lines[k]] = k
    return mapwords

def get_word_mapReverse():
    f = open('words.txt','r')
    lines = list(f.read().splitlines())
    mapwords = {}

    for k in range(len(lines)):
        mapwords[k] = lines[k]
    return mapwords

def get_map_key(map,word):

    mapkey = []
    for items in word:
        if map.get(items) is not None:
            mapkey.append(map.get(items))
        else:
            mapkey = mapkey

    mapkey = list(set(mapkey))
    return mapkey

def get_substring(w,x):

    string = list(itertools.permutations(w, x))
    finalString = []
    for j in string:
        finalString.append(''.join(j))
    return finalString

def remove_words(string, words):
    for p in words:
        string = string.replace(p, '',1)
    return string

def descrambler(w,k):
    dictionary = get_word_map()

def search(w,k):

    string = w
    answer = []
    k = list(k)

    map = get_word_map()  # 'word':1
    mapinverse = get_word_mapReverse()  # 1 :'word'

    idmap = {}
    wordmap = {}

    if len(k) == 0:
        yield answer
    else:
        string1 = get_substring(w,k[0])

        for i in range(len(string1)):
            stringkey =  map.get(string1[i])
            print('w',w)
            if stringkey is not None:
                answer.append(stringkey)
                neww = remove_words(w, str(string1[i]))

                print('neww',neww)

            else:
                pass
            # newk = deepcopy(k)
            # neww = remove_words(w, str(string1[i]))
            # newk.pop(0)
            # print(newk)
            # yield from search(w,k)

        print(answer)
search('hime',(2,2))
#
# t = search('hime',(2,2))
# result = list(t)


