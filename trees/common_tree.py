from collections import deque

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
        
        return self._dfs_recursive(value, self.root)

    def _dfs_recursive(self, value, node):
        print("Checking Node '{}'".format(node.value))
        if node.value == value:
            return node
        
        for n in node.children:
            res = self._dfs_recursive(value, n)
            if res:
                return res
        
        return None

    # DFS using Stack
    def dfs_with_stack(self, value):
        if not self.root:
            return None
        q = deque()
        q.append(self.root)
        while q:
            node = q.pop()
            print("Checking Node '{}'".format(node.value))
            if node.value == value:
                return node
            for child in node.children:
                q.append(child)

        return None

    def bfs(self, value):
        if not self.root:
            return None

        q = deque()
        q.append(self.root)

        while q:
            node = q.popleft()
            print("Checking Node '{}'".format(node.value))
            if node.value == value:
                return node
            for child in node.children:
                q.append(child)
        return None

    # Min
    def find_min_dfs(self):
        if not self.root:
            return None
        min = self.root.value
        return self._find_min_dfs_recursive(min, self.root)

    def _find_min_dfs_recursive(self, min, node):
        print("Checking Node '{}'".format(node.value))
        if node.value < min:
            min = node.value

        for child in node.children:
            min = self._find_min_dfs_recursive(min, child)

        return min

    def find_min_bfs(self):
        if not self.root:
            return None
        min = self.root.value
        q = deque()
        q.append(self.root)

        while q:
            node = q.popleft()
            print("Checking Node '{}'".format(node.value))
            if node.value < min:
                min = node.value
            for child in node.children:
                q.append(child)

        return min

    # Max
    def find_max_bfs(self):
        if not self.root:
            return None
        q = deque()
        q.append(self.root)
        max = self.root.value

        while q:
            node = q.popleft()
            print("Checking Node '{}'".format(node.value))
            if node.value > max:
                max = node.value
            for child in node.children:
                q.append(child)

        return max

    def find_max_dfs(self):
        if not self.root:
            return None
        max = self.root.value
        return self._find_max_dfs_recursive(max, self.root)

    def _find_max_dfs_recursive(self, max, node):
        print("Checking Node '{}'".format(node.value))
        if node.value > max:
            max = node.value

        for child in node.children:
            max = self._find_max_dfs_recursive(max, child)

        return max

    # Insert
    # Update
    # Delete
    # List
    def get_list(self):
        if not self.root:
            return []
        nodes = []
        q = deque()
        q.append(self.root)

        while q:
            node = q.popleft()
            nodes.append(node)

            for child in node.children:
                q.append(child)

        return nodes

    # Min Height
    def get_min_height(self):
        if not self.root:
            return -1

        min_height = 32000
        return self._get_min_height_recursive(0, min_height, self.root)

    def _get_min_height_recursive(self, height, min_height, node):
        height = height + 1
        print("Checking Node '{}' on height '{}' with min_height '{}'".format(node.value, height, min_height))
        if height >= min_height:
            return min_height
        if len(node.children) == 0:
            if height < min_height:
                min_height = height

        for child in node.children:
            res = self._get_min_height_recursive(height, min_height, child)
            if min_height > res:
                min_height = res

        return min_height

    # Max Height
    def get_max_height(self):
        if not self.root:
            return -1
        max_height = -1
        return self._get_max_height_recursive(0, max_height, self.root)

    def _get_max_height_recursive(self, height, max_height, node):
        height = height + 1
        print("Checking Node '{}' on height '{}' with max_height '{}'".format(node.value, height, max_height))
        if len(node.children) == 0:
            if height > max_height:
                max_height = height

        for child in node.children:
            res = self._get_max_height_recursive(height, max_height, child)
            if res > max_height:
                max_height = res

        return max_height

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
    print("DFS Searching for 6")
    print(t.dfs(6))

    print("DFS Searching for 13")
    print(t.dfs(13))

    print("DFS Searching for 15")
    print(t.dfs(15))

    print("DFS Searching for -1")
    print(t.dfs(-1))

    print("DFS Stack Searching for 6")
    print(t.dfs_with_stack(6))

    print("DFS Stack Searching for 13")
    print(t.dfs_with_stack(13))

    print("DFS Stack Searching for 15")
    print(t.dfs_with_stack(15))

    print("DFS Stack Searching for -1")
    print(t.dfs_with_stack(-1))

    print("BFS Searching for 6")
    print(t.bfs(6))

    print("BFS Searching for 13")
    print(t.bfs(13))

    print("BFS Searching for 15")
    print(t.bfs(15))

    print("BFS Searching for -1")
    print(t.bfs(-1))

    print("Find min using BFS")
    print(t.find_min_bfs())

    print("Find min using DFS")
    print(t.find_min_dfs())

    print("Find max using BFS")
    print(t.find_max_bfs())

    print("Find max using DFS")
    print(t.find_max_dfs())

    print("Get all nodes list using BFS")
    print(t.get_list())

    print("Find min height using DFS")
    print(t.get_min_height())

    print("Find max height using DFS")
    print(t.get_max_height())
