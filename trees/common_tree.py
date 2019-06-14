class Node(object):
    def __init__(self, value=0, children=[]):
        self.value = value
        self.children = children

    def __repr__(self):
        return "Node '{}'".format(self.value)

class Tree(object):
    def __init__(self, root):
        self.root = root
    
    def dfs(self, value):
        if not self.root:
            return None
        
        return self.dfs_recursive(value, self.root)

    def dfs_recursive(self, value, node):
        print("Checking Node '{}'".format(node.value))
        if node.value == value:
            return node
        
        for n in node.children:
            res = self.dfs_recursive(value, n)
            if res:
                return res
        
        return None

if __name__ == "__main__":
    n13 = Node(value=13)
    n12 = Node(value=12)
    n11 = Node(value=11)
    n10 = Node(value=10)
    n9 = Node(value=9)
    n8 = Node(value=8, children=[n12, n13])
    n7 = Node(value=7)
    n6 = Node(value=6, children=[n10, n11])
    n5 = Node(value=5)
    n4 = Node(value=4, children=[n9])
    n3 = Node(value=3, children=[n7, n8])
    n2 = Node(value=2, children=[n6])
    n1 = Node(value=1, children=[n4, n5])
    n0 = Node(value=0, children=[n1, n2, n3])

    t = Tree(n0)
    print("Searching for 6")
    print(t.dfs(6))

    print("Searching for 13")
    print(t.dfs(13))

    print("Searching for 15")
    print(t.dfs(15))

    print("Searching for -1")
    print(t.dfs(-1))
