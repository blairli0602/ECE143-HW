import itertools as it
from collections import defaultdict

def count_paths(m,n,blocks):

    matrix = create_matrix(m,n,blocks)
    #tree1 = build_tree1((0,0),m,n,matrix)
    #tree = build_tree(dic)

    tree1 = build_tree1((0,0),m,n,blocks)
    print(tree1)

    dic = build_dic( m, n, matrix)
    tree = build_tree(dic)
    print('dictionary',dic)
    print(tree)

    answer = 0
    # print(search(tree,0,0,m-1,n-1,answer))

    return

def create_matrix(m,n,blocks):

    m = [[0 for i in range(n)] for j in range(m)]
    for i in blocks:
        m[i[0]][i[1]] = 1

    return m

def build_tree(dic):

    d = dic
    nodelists = dict((node, [node, []]) for node in d.keys())
    for node, children in d.items():
        for child in children:
            nodelists[node][1].extend([child])

    return nodelists


def search(tree,start1,start2,m,n,pre):

    for len1 in range(2):
        for len2 in range(len(tree[(start1,start2)])):
            if start1 == m and start2 == n:
                answer = pre + 1
                return answer
            else:
                    item = tree[(start1, start2)][len2]
                    start1,start2 = item[0],item[1]
                    search(tree,start1,start2,m,n,pre)

def build_dic(m,n,matrix):

    dic = defaultdict(list)

    for i in range(m): #3
        for j in range(n): #4
            if matrix[i][j] != 1:
                if i != m-1 and j != n-1:
                    if matrix[i][j + 1] == 0:
                        dic[(i, j)].append([i, j + 1])
                    if matrix[i + 1][j] == 0:
                        dic[(i, j)].append([i + 1, j])
                if i == m-1 and j != n-1:
                    if matrix[i][j + 1] == 0:
                        dic[(i, j)].append([i, j + 1])
                if j == n-1 and i != m-1:
                    if matrix[i+1][j] == 0:
                        dic[(i, j)].append([i+1, j])

    return dic

def build_tree1(point, m, n, blocks):

    tree = dict()

    tree[point] = list()
    for neighbor in neighbors(point, m, n, blocks):
        tree[point].append(build_tree1(neighbor, m, n, blocks))

    return tree


def neighbors(point, m, n, blocks):
    """
    yields neighbors of a point
    :param point:
    :return:
    """
    candidates = (point[0]+1, point[1]), (point[0], point[1]+1)

    for candidate in candidates:
        if candidate[0] <= m and candidate[1] <= n and candidate not in blocks:
            yield candidate


x = count_paths(3,4,[(0,3),(1,1)])
print(x)