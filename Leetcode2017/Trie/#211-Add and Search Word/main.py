# coding=utf-8

'''
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only 
letters a-z or .. A . means it can represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
'''

'''
注意休止符，还有搜索关键词长度超过深度的情况
Beat 73.61%
公司：Facebook
'''

class WordDictionary(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for char in word:
            cur = cur.setdefault(char, {})
        cur['#'] = {}

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        n = len(word)
        cur = self.root
        q = collections.deque([[cur, 0]])

        while q:
            cur_dict, step = q.pop()
            if step == n and cur_dict.has_key('#'):
                return True
            if step >= n:
                continue
            if word[step] == '.':
                for value in cur_dict.values():
                    q.appendleft([value, step + 1])
            elif cur_dict.has_key(word[step]):
                q.appendleft([cur_dict[word[step]], step + 1])
        
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)