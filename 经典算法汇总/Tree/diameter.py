# coding=utf-8

'''
求二叉树的直径的方法，直径的定义是二叉树中两个相距最远的点之间的距离
朴素递归法O(n^2)，改进方法O(n)
'''

# 朴素算法先算出左右子树高，在算出左右子树直径，最后得root点直径，DC思路无误

# Python program to find the diameter of binary tree

# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


"""
The function Compute the "height" of a tree. Height is the
number f nodes along the longest path from the root node
down to the farthest leaf node.
"""
def height(node):

    # Base Case : Tree is empty
    if node is None:
        return 0 ;

    # If tree is not empty then height = 1 + max of left
    # height and right heights
    return 1 + max(height(node.left) ,height(node.right))

# Function to get the diamtere of a binary tree
def diameter(root):

    # Base Case when tree is empty
    if root is None:
        return 0;

    # Get the height of left and right sub-trees
    lheight = height(root.left)
    rheight = height(root.right)

    # Get the diameter of left and irgh sub-trees
    ldiameter = diameter(root.left)
    rdiameter = diameter(root.right)

    # Return max of the following tree:
    # 1) Diameter of left subtree
    # 2) Diameter of right subtree
    # 3) Height of left subtree + height of right subtree +1
    return max(lheight + rheight + 1, max(ldiameter, rdiameter))


# Driver program to test above functions

"""
Constructed binary tree is
            1
          /   \
        2      3
      /  \
    4     5
"""

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print "Diameter of given binary tree is %d" %(diameter(root))

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)

'''
下面是优化版的C代码
'''

'''
/*The second parameter is to store the height of tree.
   Initially, we need to pass a pointer to a location with value
   as 0. So, function should be used as follows:

   int height = 0;
   struct node *root = SomeFunctionToMakeTree();
   int diameter = diameterOpt(root, &height); */
int diameterOpt(struct node *root, int* height)
{
  /* lh --> Height of left subtree
     rh --> Height of right subtree */
  int lh = 0, rh = 0;

  /* ldiameter  --> diameter of left subtree
     rdiameter  --> Diameter of right subtree */
  int ldiameter = 0, rdiameter = 0;

  if(root == NULL)
  {
    *height = 0;
     return 0; /* diameter is also 0 */
  }

  /* Get the heights of left and right subtrees in lh and rh
    And store the returned values in ldiameter and ldiameter */
  ldiameter = diameterOpt(root->left, &lh);
  rdiameter = diameterOpt(root->right, &rh);

  /* Height of current node is max of heights of left and
     right subtrees plus 1*/
  *height = max(lh, rh) + 1;

  return max(lh + rh + 1, max(ldiameter, rdiameter));
}
'''
