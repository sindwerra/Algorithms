# coding=utf-8

'''
一种很神奇的数据结构...
'''

def getsum(BITTree,i):
    res = 0
    # index in BITree[] is 1 more than the index in arr[]
    i = i+1
    while i > 0:

        # Add current element of BITree to sum
        res += BITTree[i]

        # Move index to parent node in getSum View
        i -= i & (-i)
    return res

# Updates a node in Binary Index Tree (BITree) at given index
# in BITree.  The given value 'val' is added to BITree[i] and
# all of its ancestors in tree.
def updatebit(BITTree , n , i ,v):
    # index in BITree[] is 1 more than the index in arr[]
    i += 1
    while i <= n:
        # Add 'val' to current node of BI Tree
        BITTree[i] += v
        # Update index to that of parent in update View
        i += i & (-i)

# Constructs and returns a Binary Indexed Tree for given
# array of size n.
def construct(arr, n):
    BITTree = [0]*(n+1)
    for i in range(n):
        updatebit(BITTree, n, i, arr[i])
    return BITTree


# Driver code to test above methods
freq = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
BITTree = construct(freq,len(freq))
print "Sum of elements in arr[0..5] is " + str(getsum(BITTree,5))
freq[3] += 6
updatebit(BITTree, len(freq), 3, 6)
print "Sum of elements in arr[0..5] is " + str(getsum(BITTree,5))
