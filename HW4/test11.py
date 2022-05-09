import itertools

def get_substring(w,x):

    string = list(itertools.permutations(w, x))
    finalString = []
    for j in string:
        finalString.append(''.join(j))
    return finalString

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

def remove_words(string, words):
    for p in words:
        string = string.replace(p, '',1)
    return string

def get_map_key(map,word):

    mapkey = []
    for items in word:
        if map.get(items) is not None:
            mapkey.append(map.get(items))
        else:
            mapkey = mapkey

    mapkey = list(set(mapkey))
    return mapkey

def get_output(x):
    final = []
    xkeys = list(x.keys())
    xitems = list(x.values())
    for i in range(len(xkeys)):
        string1 = xkeys[i]
        for j in range(len(xitems[i])):
            for k in range(len(xitems[i][j])):
                finalstring = str(string1) + ' ' + str(xitems[i][j])
                if finalstring not in final:
                    final.append(finalstring)
    return final


def descrambler(w,k):

    k = list(k)
    string1 = get_substring(w,k[0])
    substring = []

    print(string1)

    for i in string1:
        w1 = remove_words(w, i)
        if len(k) > 1:
            string2 = get_substring(w1,k[0])
            substring.append(string2)
            k.pop(0)

        else:
            break


    print(substring)

    map = get_word_map() #'word':1
    mapinverse = get_word_mapReverse() # 1 :'word'

    idmap = {}
    wordmap = {}
    for i in range(len(string1)):
        stringkey = map.get(string1[i])
        substringmap = get_map_key(map, substring[i])
        if stringkey is not None and substringmap != []:
            idmap[stringkey] = substringmap

    for key,val in idmap.items():
        if mapinverse.get(key) is not None:
            wordmap[mapinverse.get(key)] = get_map_key(mapinverse,val)

    finalstring = get_output(wordmap)

    return finalstring


result = descrambler('trleeohelh',(5,5))
print(result)