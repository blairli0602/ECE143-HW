from time import sleep
import random
from datetime import datetime
import itertools as it

def producer():
    'produce timestamps'
    starttime = datetime.now()
    while True:
        sleep(random.uniform(0, 0.2))
        yield datetime.now() - starttime

def tracker(p,limit):

    """
    tracks the output of this producer and ultimately returns the number of odd numbered seconds that have been iterated over, up until the limit number

    param p: generator p
    param limit: number of maximum run, int
    returns: list
    """

    assert limit > 0

    nlimit = yield limit

    if nlimit is None:
        nlimit = limit
    else:
        nlimit = nlimit
    result = 0

    while result < nlimit:
        p = producer()
        x = next(p)
        sec = x.total_seconds()
        sec = int(sec * 1000000)

        if sec % 2 == 0:
            result = result + 1
            yield result
        else:
            result = result
            yield result


p = producer()
next(p)
t = tracker(p, 5)
next(t)
t.send(9)


#t.send(9)
result = list(t)

print(result)

