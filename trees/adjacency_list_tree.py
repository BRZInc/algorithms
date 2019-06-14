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
    
    def search(self, value):
        if not self.nodes:
            return None
        return self.nodes.get(value, -1)

    def dfs(self):
        # if not self.root:
        #     return -1
        if not self.nodes:
            return -1
        
        node_index = self.root
        self._dfs_recursive(node_index)
    
    def _dfs_recursive(self, node_index):
        print("Checking Node '{}'".format(node_index))
        node = self.nodes.get(node_index)
        if not node:
            return
        for child in node:
            self._dfs_recursive(child)

if __name__ == "__main__":
    nodes = {
        0: [1, 2, 3],
        1: [4, 5],
        2: [6],
        3: [7, 8],
        4: [9],
        5: None,
        6: [10, 11],
        7: None,
        8: [12, 13],
        9: None,
        10: [14, 15],
        11: None,
        12: None,
        13: None,
        14: None,
        15: None
    }
    t = AdjacencyListTree(0, nodes)

    print("Searching for 6")
    print(t.search(6))

    print("Searching for 13")
    print(t.search(13))

    print("Searching for 15")
    print(t.search(15))

    print("Searching for -1")
    print(t.search(-1))

    print("DFS Walkthrough")
    t.dfs()

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