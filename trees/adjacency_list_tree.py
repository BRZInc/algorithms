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
    
    def bfs(self, value):
        if not self.nodes:
            return -1
        q = deque()
        q.append(self.root)

        while q:
            node_index = q.popleft()
            node = self.nodes[node_index]
            print("Checking Node '{}'".format(node_index))

            if node.value == value:
                return node

            if not node.children:
                continue

            for child_index in node.children:
                q.append(child_index)

        return None

    def find_min_dfs(self):
        if not self.nodes:
            return None

        min = 32000
        return self._find_min_dfs_recursive(min, self.root)

    def _find_min_dfs_recursive(self, min, node_index):
        node = self.nodes.get(node_index)
        print("Checking Node '{}'".format(node_index))
        if not node:
            return None
        if node.value < min:
            min = node.value

        for child_index in node.children:
            res = self._find_min_dfs_recursive(min, child_index)
            if res and res < min:
                min = res

        return min

    def find_min_bfs(self):
        if not self.nodes:
            return None

        q = deque()
        q.append(self.root)

        min = 32000

        while q:
            node_index = q.popleft()
            print("Checking Node '{}'".format(node_index))
            node = self.nodes[node_index]
            if node.value < min:
                min = node.value
            for child_index in node.children:
                q.append(child_index)

        return min

    def find_max_dfs(self):
        if not self.nodes:
            return None

        max = 0
        return self._find_max_dfs_recursive(max, self.root)

    def _find_max_dfs_recursive(self, max, node_index):
        node = self.nodes.get(node_index)
        print("Checking Node '{}'".format(node_index))

        if not node:
            return None
        if node.value > max:
            max = node.value

        for child_index in node.children:
            res = self._find_max_dfs_recursive(max, child_index)
            if res and res > max:
                max = res

        return max

    def find_max_bfs(self):
        if not self.nodes:
            return None
        q = deque()
        q.append(self.root)
        max = 0

        while q:
            node_index = q.popleft()
            print("Checking Node '{}'".format(node_index))
            node = self.nodes[node_index]
            if node.value > max:
                max = node.value
            for child_index in node.children:
                q.append(child_index)

        return max

    def get_list(self):
        return [node for key, node in self.nodes.items()]

    def get_min_height(self):
        if not self.nodes:
            return None

        min_height = 32000
        return self._get_min_height_recursive(0, min_height, self.root)

    def _get_min_height_recursive(self, height, min_height, node_index):
        node = self.nodes.get(node_index)
        height = height + 1
        print("Checking Node '{}' with height '{}' and min_height '{}'".format(node_index, height, min_height))
        if not node:
            return None
        if len(node.children) == 0:
            if height < min_height:
                min_height = height

        for child_index in node.children:
            res = self._get_min_height_recursive(height, min_height, child_index)
            if res and res < min_height:
                min_height = res

        return min_height

    def get_max_height(self):
        if not self.nodes:
            return None

        height = 0
        max_height = 0
        return self._get_max_height_recursive(height, max_height, self.root)

    def _get_max_height_recursive(self, height, max_height, node_index):
        height = height + 1
        node = self.nodes[node_index]
        print(
            "Checking Node '{}' with height '{}' and max_height '{}'".format(
                node_index, height, max_height))
        if len(node.children) == 0:
            if max_height < height:
                max_height = height

        for child_index in node.children:
            res = self._get_max_height_recursive(height, max_height, child_index)
            if res and res > max_height:
                max_height = res

        return max_height

    # Count
    def get_count_bfs(self):
        q = deque()
        q.append(self.root)
        count = 0

        while q:
            node_index = q.popleft()
            node = self.nodes[node_index]
            count +=1
            for child_index in node.children:
                q.append(child_index)

        return count

    def get_count_dfs(self):
        if not self.nodes:
            return None

        count = 0
        return self._get_count_dfs_recursive(count, self.root)

    def _get_count_dfs_recursive(self, count, node_index):
        print("Checking Node '{}'".format(node_index))
        node = self.nodes[node_index]
        count += 1

        for child_index in node.children:
            count += self._get_count_dfs_recursive(0, child_index)

        return count

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

    print("BFS Searching for 40")
    print(t.bfs(40))

    print("BFS Searching for 70")
    print(t.bfs(70))

    print("BFS Searching for 90")
    print(t.bfs(90))

    print("BFS Searching for 0")
    print(t.bfs(0))

    print("Find min using BFS")
    print(t.find_min_bfs())

    print("Find min using DFS")
    print(t.find_min_dfs())

    print("Find max using BFS")
    print(t.find_max_bfs())

    print("Find max using DFS")
    print(t.find_max_dfs())

    print("Get all nodes list")
    print(t.get_list())

    print("Find min height using DFS")
    print(t.get_min_height())

    print("Find max height using DFS")
    print(t.get_max_height())

    print("Total count using BFS")
    print(t.get_count_bfs())

    print("Total count using DFS")
    print(t.get_count_dfs())