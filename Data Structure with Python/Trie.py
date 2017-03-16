# coding=utf-8

'''
实现前缀树，一种经典的数据结构
这里用的是网上看的最容易实现的nested dictionary方法
还有传统的树型结构没有实现
Beat 97.81%
公司：Google, Uber, Facebook, Twitter, Microsoft, Bloomberg
'''

'''
Implement a trie with insert, search, and startsWith methods.
'''

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.end = '$'

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        currentdict = self.root
        for letter in word:
            currentdict = currentdict.setdefault(letter, {})
        currentdict[self.end] = self.end

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        tmp = self.root
        for letter in word:
            if tmp.has_key(letter):
                tmp = tmp[letter]
            else:
                return False

        if tmp.has_key(self.end):
            return True
        else:
            return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        tmp = self.root
        for letter in prefix:
            if tmp.has_key(letter):
                tmp = tmp[letter]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
