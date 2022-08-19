# coding=utf-8

'''
Given n processes, each process has a unique PID (process id) and its PPID 
(parent process id).

Each process only has one parent process, but may have one or more children processes. 
This is just like a tree structure. Only one process has PPID that is 0, 
which means this process has no parent process. All the PIDs will be distinct 
positive integers.

We use two list of integers to represent a list of processes, where the first 
list contains PID for each process and the second list contains the corresponding PPID.

Now given the two lists, and a PID representing a process you want to kill, 
return a list of PIDs of processes that will be killed in the end. 
You should assume that when a process is killed, all its children processes 
will be killed. No order is required for the final answer.

Example 1:
Input: 
pid =  [1, 3, 10, 5]
ppid = [3, 0, 5, 3]
kill = 5
Output: [5,10]
Explanation: 
           3
         /   \
        1     5
             /
            10
Kill 5 will also kill 10.
Note:
The given kill id is guaranteed to be one of the given PIDs.
n >= 1.
'''

'''
这道题可以用哈希表模拟图之后的DFS或者BFS来做，leetcode上面还有直接模拟树的解法
Beat 100%
公司：Bloomberg
'''

class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        store = {}
        n = len(pid)
        result = []

        for i in xrange(n):
            store.setdefault(ppid[i], [])
            store[ppid[i]].append(pid[i])

        if kill in store:
            self.DFS(store, kill, result)
        
        for i in xrange(n):
            if pid[i] == kill and pid[i] not in store:
                result.append(pid[i])
                
        return result

    def DFS(self, store, target, result):
        result.append(target)
        for child in store[target]:
            if child not in store:
                result.append(child)
                continue
            self.DFS(store, child, result)
    

        
