"""
更正统的一版解法，使用字典来将无向图完全的模拟出来，然后再进行一次DFS操作，所以这里的技术是正向计数
"""


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        store = collections.defaultdict(list)
        for start, end in edges:
            store[start].append(end)
            store[end].append(start)

        parent = [-1] * n
        result = 0
        for i in range(n):
            if parent[i] == -1:
                self.find(parent, store, i)
                result += 1
        return result

    def find(self, parent, store, node):
        if parent[node] != -1:
            return
        parent[node] = 1
        for neighbor in store[node]:
            if neighbor in store:
                self.find(parent, store, neighbor)
