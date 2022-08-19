'''
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have
to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it
possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have
finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have
finished course 0, and to take course 0 you should also have finished course 1.
So it is impossible.

Note:
The input prerequisites is a graph represented by a list of edges,
not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
click to show more hints.

Hints:
This problem is equivalent to finding if a cycle exists in a directed graph.
If a cycle exists, no topological ordering exists and therefore it will be
impossible to take all courses.
Topological Sort via DFS - A great video tutorial (21 minutes) on
Coursera explaining the basic concepts of Topological Sort.
Topological sort could also be done via BFS.
'''

'''
此题可以用BFS也可以用DFS做，能完成所有课程的实质就是此图里面无环，有环就没办法完成
下面是DFS的方法，但是DFS方法在大数据情况下可能造成栈击穿，BFS没有这种问题
和无向图相比需要加一个recstack保存当前探索过的所有verticle
Beat 80.16%
公司：Apple, Yelp, Zenefits
'''

class Solution(object):
    def DFS_visit(self, key, color, store, recStack):
        color[key], recStack[key] = 1, 1
        for node in store[key]:
            if not store.has_key(node):
                continue
            if recStack[node]:
                return True
            elif not color[node] and self.DFS_visit(node, color, store, recStack):
                return True
        recStack[key] = 0
        return False

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        store = {}
        for cur, pre in prerequisites:
            store.setdefault(pre, [])
            store[pre].append(cur)

        color = [0] * numCourses
        recStack = [0] * numCourses
        for key in range(numCourses):
            if not store.has_key(key):
                continue
            if not color[key]:
                tmp = self.DFS_visit(key, color, store, recStack)
                if tmp:
                    return False
        return True
