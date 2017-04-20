# coding=utf-8

'''
这题确实是难... 首先合适的数据结构就很难想到(第一种是双向链表搭配哈希表，第二种是单向链表搭配哈希表，
但是第二种需要哈希表的指向永远指向对应点的前一个节点，需要有很多额外的算法处理)，其次对应的结构找到之后还必须
对指针进行很小心的处理，如get的是最后一个尾节点和set一个已有节点这两种特殊情况如何更新链表，最后在capacity
满时删除头节点必须真正删除，也就意味着不仅在哈希表里删除这个key，也要将这个node真正的删除掉，而要找到这个
node的key，必须额外再用一个哈希表node_key将node和key的映射反过来一一保存，假删除(不用node_key哈希表而
是直接将删除结点的值改为-1然后丢下不管)是不行的，会有run time error出现. 另外这题也证明了抽象过程有
多么重要
Beat 81.05%
公司：Google, Uber, Facebook, Twitter, Zenefits, Amazon, Microsoft, Snapchat, Yahoo, Bloomberg, Palantir
'''


class LRUCache(object):
    
    class ListNode(object):
        def __init__(self, x=None):
            self.next = None
            self.prev = None
            self.val = x

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.root = ListNode('dummy')
        self.tail = self.root
        self.key_node = {}
        self.node_key = {}
        self.count = 0
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if not self.key_node.has_key(key):
            return -1

        result = self.key_node[key].val
        self.update(self.key_node[key])
        return result

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.key_node.has_key(key):
            self.key_node[key].val = value
            self.update(self.key_node[key])
        else:
            self.append(key, value)
            self.count += 1

            if self.count > self.capacity:
                self.count -= 1
                self.delete()

    def update(self, root):
        if root == self.tail:
            return
        
        parent = root.prev
        son = root.next
        parent.next = son
        son.prev = parent
        root.prev = self.tail
        root.next = None
        self.tail.next = root
        self.tail = self.tail.next

    def delete(self):
        tmp = self.root.next
        self.root.next = tmp.next
        tmp.next.prev = self.root
        tmp.next = None
        tmp.prev = None
        key = self.node_key[tmp]
        del self.key_node[key]
        del self.node_key[tmp]

    def append(self, key, value):
        self.key_node[key] = ListNode(value)
        self.node_key[self.key_node[key]] = key
        self.tail.next = self.key_node[key]
        self.key_node[key].prev = self.tail
        self.tail = self.tail.next


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)