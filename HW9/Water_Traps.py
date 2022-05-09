def get_trapped_water(seq):
    """
    Calculates the amount of water trapped between walls
    :param seq:
    :return:
    """

    assert len(seq) > 0
    assert isinstance(seq,list)
    for item in seq:
        assert item >= 0
        assert isinstance(item, int)

    n = len(seq)
    answer = maxWater(seq,n)
    return answer

def maxWater(arr, n):

    res = 0
    # For every element of the array
    for i in range(1, n - 1):

        # Find the maximum element on its left
        left = arr[i]
        for j in range(i):
            left = max(left, arr[j])

        # Find the maximum element on its right
        right = arr[i];

        for j in range(i + 1, n):
            right = max(right, arr[j])

        # Update the maximum water
        res = res + (min(left, right) - arr[i])

    return res

seq = [3, 0, 1, 3, 0, 5]


print(get_trapped_water(seq))