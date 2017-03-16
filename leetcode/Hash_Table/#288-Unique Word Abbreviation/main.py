# coding=utf-8

'''
An abbreviation of a word follows the form <first letter><number><last letter>.
Below are some examples of word abbreviations:

a) it                      --> it    (no abbreviation)

     1
b) d|o|g                   --> d1g

              1    1  1
     1---5----0----5--8
c) i|nternationalizatio|n  --> i18n

              1
     1---5----0
d) l|ocalizatio|n          --> l10n
Assume you have a dictionary and given a word, find whether its abbreviation
is unique in the dictionary. A word's abbreviation is unique if no other
word from the dictionary has the same abbreviation.

Example:
Given dictionary = [ "deer", "door", "cake", "card" ]

isUnique("dear") ->
false

isUnique("cart") ->
true

isUnique("cane") ->
false

isUnique("make") ->
true
'''

'''
这题题干描述太失真了，再加上一些奇怪的boundary case，其实有点复杂
Beat 66.95%
'''

class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.store = dictionary
        self.jisho = {}
        tmp = None
        for s in self.store:
            n = len(s)
            if 0 < n <= 2:
                tmp = s
            elif not n:
                continue
            else:
                tmp = s[0] + str(n - 2) + s[-1]
            if self.jisho.has_key(tmp):
                if s in self.jisho[tmp]:
                    continue
                self.jisho[tmp].append(s)
            else:
                self.jisho[tmp] = [s]

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        n = len(word)
        if n <= 2:
            if self.jisho.has_key(word):
                return len(self.jisho[word]) == 1 and word in self.jisho[word]
            return True
        else:
            tmp = word[0] + str(n - 2) + word[-1]
            if self.jisho.has_key(tmp):
                return len(self.jisho[tmp]) == 1 and word in self.jisho[tmp]
            return True

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
