from collections import deque

class Node(object):
    def __init__(self, value, id, children=[]):
        self.value = value
        self.id = id
        self.children = children
    
    def __repr__(self):
        return "<Node id='{}' value='{}'>".format(self.id, self.value)

"""
    + Quick access to elements
    + Small amount of required memory
    + May additionally wrap nodes into classes to store extra info
    - Complicated to change
"""
class AdjacencyListTree(object):
    def __init__(self, root, nodes_dict):
        self.root = root
        self.nodes = nodes_dict
    
    def search_by_id(self, id):
        if not self.nodes:
            return None
        return self.nodes.get(id, None)

    def dfs(self, value):
        # if not self.root:
        #     return -1
        if not self.nodes:
            return None

        return self._dfs_recursive(self.root, value)
    
    def _dfs_recursive(self, node_id, value):
        print("Checking Node '{}'".format(node_id))
        node = self.nodes.get(node_id)

        if not node:
            return None
        if node.value == value:
            return node
        for child_id in node.children:
            res = self._dfs_recursive(child_id, value)
            if res:
                return res

        return None
    
    def bfs(self):
        if not self.nodes:
            return -1
        q = deque()
        q.append(self.root)

        while q:
            node_index = q.popleft()
            print("Checking Node '{}'".format(node_index))
            children = self.nodes.get(node_index)
            if not children:
                continue
            for child_index in children:
                q.append(child_index)

if __name__ == "__main__":
    nodes = {
        0: Node(id=0, value=5, children=[1, 2, 3]),
        1: Node(id=1, value=10, children=[4, 5]),
        2: Node(id=2, value=15, children=[6]),
        3: Node(id=3, value=20, children=[7, 8]),
        4: Node(id=4, value=25, children=[9]),
        5: Node(id=5, value=30),
        6: Node(id=6, value=35, children=[10, 11]),
        7: Node(id=7, value=40),
        8: Node(id=8, value=45, children=[12, 13]),
        9: Node(id=9, value=50),
        10: Node(id=10, value=55, children=[14, 15]),
        11: Node(id=11, value=60),
        12: Node(id=12, value=60),
        13: Node(id=13, value=65),
        14: Node(id=14, value=70),
        15: Node(id=15, value=75)
    }
    t = AdjacencyListTree(0, nodes)

    print("Searching for 6")
    print(t.search_by_id(6))

    print("Searching for 13")
    print(t.search_by_id(13))

    print("Searching for 15")
    print(t.search_by_id(15))

    print("Searching for -1")
    print(t.search_by_id(-1))

    print("DFS Search for 40")
    print(t.dfs(40))

    print("DFS Search for 70")
    print(t.dfs(70))

    print("DFS Search for 90")
    print(t.dfs(90))

    print("DFS Search for 0")
    print(t.dfs(0))

    # print("BFS Search for 40")
    # t.bfs()

    # print("DFS Stack Searching for 6")
    # print(t.dfs_with_stack(6))

    # print("DFS Stack Searching for 13")
    # print(t.dfs_with_stack(13))

    # print("DFS Stack Searching for 15")
    # print(t.dfs_with_stack(15))

    # print("DFS Stack Searching for -1")
    # print(t.dfs_with_stack(-1))

    # print("BFS Searching for 6")
    # print(t.bfs(6))

    # print("BFS Searching for 13")
    # print(t.bfs(13))

    # print("BFS Searching for 15")
    # print(t.bfs(15))

    # print("BFS Searching for -1")
    # print(t.bfs(-1))

    # print("Find min using BFS")
    # print(t.find_min_bfs())

    # print("Find min using DFS")
    # print(t.find_min_dfs())

    # print("Find max using BFS")
    # print(t.find_max_bfs())

    # print("Find max using DFS")
    # print(t.find_max_dfs())

    # print("Get all nodes list using BFS")
    # print(t.get_list())

    # print("Find min height using DFS")
    # print(t.get_min_height())

    # print("Find max height using DFS")
    # print(t.get_max_height())