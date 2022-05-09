class Node:
    def __init__(self, val:int=0, left=None, right=None):
        assert isinstance(left, Node) or left is None
        assert isinstance(right, Node) or right is None
        self.val = val
        self.left = left
        self.right = right

    def insert(self,data):
        if self.val:
            if data < self.val:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.val:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.val = data

def findParent(node: Node,val: int, parent: int) -> None:
    """
    :node:node
    val: target
    """
    if (node is None):
        pass
    elif (node.val == val):
        yield parent
    else:
        yield from findParent(node.left, val, node.val)
        yield from findParent(node.right, val, node.val)

def get_tree_list(p:list[int]):
    """
    :a: p input list
    """
    assert isinstance(p, list)
    for i in p:
        assert isinstance(i,int)
    assert len(set(p)) == len(p)
    assert len(p) > 0

    root = Node(p[0])
    for i in range(1, len(p)):
        root.insert(p[i])

    final = []
    for j in range(len(p)):
        result = list(findParent(root,j,j))
        final.append(result[0])
    return final


p = [8, 5, 1, 10, 0, 4, 2, 3, 7, 9, 6]

result = get_tree_list(p)
print(result)



