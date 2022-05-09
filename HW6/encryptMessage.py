import string
import random

def book(fname):

    f = open(fname,'r')
    lines = list(f.readlines())
    result = []
    dic = {}

    for line in lines:
        newline = line.translate(str.maketrans('', '', string.punctuation)).lower()
        result.append(newline)

    for num, line in enumerate(result, 1):
        for index, word in enumerate(line.split(), 1):
            if word in dic.keys():
                dic[word].append((num,index))
            else:
                dic[word] = [(num,index)]

    return dic

def encrypt_message(message,fname):
    '''
    Given `message`, which is a lowercase string without any punctuation, and `fname` which is the
    name of a text file source for the codebook, generate a sequence of 2-tuples that
    represents the `(line number, word number)` of each word in the message. The output is a list
    of 2-tuples for the entire message. Repeated words in the message should not have the same 2-tuple.
    :param message: message to encrypt
    :type message: str
    :param fname: filename for source text
    :type fname: str
    :returns: list of 2-tuples
    '''
    assert isinstance(message,str)
    assert isinstance(fname,str)
    assert fname[-4:] == '.txt'

    newMessage = message.translate(str.maketrans('', '', string.punctuation)).lower()
    book_map = book(fname)
    result = []

    for i in list(newMessage.split()):
        if len(book_map[i]) == 1:
            result.append(book_map[i][0])
        elif len(book_map[i]) != 1:
            cho = tuple(random.choice(book_map[i]))
            result.append(cho)

    return result

def decrypt_message(inlist,fname):
    '''
    Given `inlist`, which is a list of 2-tuples`fname` which is the
    name of a text file source for the codebook, return the encrypted message.

    :param message: inlist to decrypt
    :type message: list
    :param fname: filename for source text
    :type fname: str
    :returns: string decrypted message
    '''

    assert isinstance(inlist, list)
    for items in inlist:
        assert isinstance(items,tuple)

    book_map = book(fname)
    result = []

    keys = list(book_map.keys())
    values = list(book_map.values())

    for i in inlist:
       for key,value in book_map.items():
           if i in value:
               result.append(key)

    result1 = ' '.join(result)
    return result1

n = 'let us not say we met late at the night about the secret'
print(encrypt_message(n,'lines.txt'))

y = encrypt_message(n,'lines.txt')
print(decrypt_message(y,'lines.txt'))