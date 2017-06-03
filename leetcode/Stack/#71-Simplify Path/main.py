# coding=utf-8

'''
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
click to show corner cases.

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple 
slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".
'''

'''
没有规律，这种怎么搞啊
公司：Microsoft, Facebook
Beat 48.68%
'''

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        lst = [x for x in path.replace('//', '/').strip().split('/') if x != '']

        result = ''
        count = 0
        while lst:
            tmp = ''
            while lst and lst[-1] == '..':
                lst.pop()
                count += 1
            while lst and count:
                parent = lst.pop()
                if parent == '.':
                    continue
                if parent == '..':    
                    count += 1
                    continue
                count -= 1
            if lst:
                tmp = lst.pop()
                if tmp == '..':
                    count += 1
                    continue
                result = tmp + result if tmp != '.' else result
                result = '/' + result if tmp != '.' else result
        return '/' + result if result == '' else result