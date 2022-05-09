def next_permutation(t:tuple)-> tuple :

    """
    next_permutation
    :t: tuple
    :return: tuple

    """
    assert isinstance(t,tuple)
    assert len(set(t)) == len(t)
    for i in t:
        assert isinstance(i, int)

    t = list(t)
    result = t
    left = find_max_left(t)
    if sorted(t,reverse=True) == t:
        return tuple(sorted(t))
    else:
        right = find_max_right(t,left)
        t[left],t[right] = t[right],t[left]
        result[left+1:] = sorted(t[left+1:])
        return tuple(result)

def find_max_left(t):

    left = 0
    right = left + 1

    for i in range(len(t)-1):
        if sorted(t,reverse=True) == t:
            return left
        elif t[i] < t[i+1]:
            left = i
            right = left + 1
        else:
            left = left
            right = right

    return left

def find_max_right(t,l):

    for i in range(l+1,len(t)):

        if t[l] < t[i]:
            right = i
        else:
            right = right

    return right

print(next_permutation((2,3,1))) #b --> 312