/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

// C++采用的是递归法并通过缩减最大最小值界限来判断BST成立与否，速度明显更快

class Solution {
public:
    bool isValidBST(TreeNode* root) {
        return checkBST(root, LONG_MIN, LONG_MAX);
    }

    bool checkBST(TreeNode *ptr, long min, long max) {
        if (ptr == NULL) {
            return true;
        }

        long val = ptr->val;

        if (val >= max || val <= min) {
            return false;
        }

        return checkBST(ptr->left, min, val) && checkBST(ptr->right, val, max);
    }
};
