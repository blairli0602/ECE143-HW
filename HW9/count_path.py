def count_paths(m,n,blocks):

    """
    Counts the number of path
    :param m:
    :param n:
    :param blocks:
    :return:
    """
    assert isinstance(m, int)
    assert m > 0
    assert isinstance(n, int)
    assert n > 0

    matrix = create_matrix(m, n, blocks)
    i = 0
    j = 0

    for item in blocks:
        assert isinstance(item, tuple)
        assert isinstance(item[0], int)
        assert 0 <= item[0] < m
        assert isinstance(item[1], int)
        assert 0 <= item[1] < n

    answer = list(countPaths(matrix,i,j, m, n))
    return len(answer)

def create_matrix(m,n,blocks):

    m = [[0 for i in range(n)] for j in range(m)]
    for i in blocks:
        m[i[0]][i[1]] = 1

    return m

def countPaths(matrix,i,j, m, n):

    if (i == m-1 and j == n-1):
        yield 1

    else:
        if i != m - 1 and j != n - 1:
            if matrix[i][j + 1] == 0:
                yield from countPaths(matrix, i, j + 1, m, n)
            if matrix[i + 1][j] == 0:
                yield from countPaths(matrix, i+1, j, m, n)
        if i == m - 1 and j != n - 1:
            if matrix[i][j + 1] == 0:
                yield from countPaths(matrix, i, j + 1, m, n)
        if j == n - 1 and i != m - 1:
            if matrix[i + 1][j] == 0:
                yield from countPaths(matrix, i + 1, j, m, n)

x = count_paths(3,4,[(0,3),(1,1)])

print(x)