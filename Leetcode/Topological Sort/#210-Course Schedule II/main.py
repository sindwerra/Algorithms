# coding=utf-8

'''
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to
first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the
ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them.
If it is impossible to finish all courses, return an empty array.

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have
finished course 0. So the correct course order is [0,1]

4, [[1,0],[2,0],[3,1],[3,2]]
There are a total of 4 courses to take. To take course 3 you should have
finished both courses 1 and 2. Both courses 1 and 2 should be taken after
you finished course 0. So one correct course order is [0,1,2,3]. Another
correct ordering is[0,2,1,3].

Note:
The input prerequisites is a graph represented by a list of edges,
not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
click to show more hints.

Hints:
This problem is equivalent to finding the topological order in a directed graph.
If a cycle exists, no topological ordering exists and therefore it will be
impossible to take all courses.
Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera
explaining the basic concepts of Topological Sort.
Topological sort could also be done via BFS.
'''

'''
此题是真正的topological sort，每个DFS函数调用完后，把当前起始点插入到结果栈的头部
DFS的做法在lintcode会击穿栈，必须找BFS的方法做
Beat 87.45%
公司：Facebook, Zenefits
'''

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        color, recStack = [0] * numCourses, [0] * numCourses
        store = {}
        for con, pre in prerequisites:
            store.setdefault(pre, [])
            store[pre].append(con)

        res = []
        for key in store:
            if not color[key]:
                tmp = self.DFS(key, color, recStack, store, res)
                if tmp:
                    return []
        for s in range(numCourses):
            if not color[s]:
                res.append(s)

        return res

    def DFS(self, key, color, recStack, store, res):
        color[key], recStack[key] = 1, 1
        for node in store[key]:
            if not store.has_key(node):
                continue
            if recStack[node]:
                return True
            elif not color[node] and self.DFS(node, color, recStack, store, res):
                return True

        recStack[key] = 0
        res.insert(0, key)
        return False


'''
利用出入度的方法也可以判断有向图有环无环且同时进行拓扑排序
Beat 95.59%
'''

class Solution(object):
    def findOrder(self, n, pres):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        ind = [[] for _ in xrange(n)]
        oud = [0] * n
        for p in pres:
            oud[p[0]] += 1
            ind[p[1]].append(p[0])
        ans = []
        for i in xrange(n):
            if oud[i] == 0:
                ans.append(i)
        l = 0
        while l !=  (ans):
            x = ans[l]
            l += 1
            for i in ind[x]:
                oud[i] -= 1
                if oud[i] == 0:
                    ans.append(i)
        return ans if l == n else []
