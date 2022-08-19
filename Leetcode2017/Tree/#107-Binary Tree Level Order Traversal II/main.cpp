// coding=utf-8

// Given a binary tree, return the bottom-up level order
// traversal of its nodes' values. (ie, from left to right,
//   level by level from leaf to root).
//
// For example:
// Given binary tree [3,9,20,null,null,15,7],
//     3
//    / \
//   9  20
//     /  \
//    15   7
// return its bottom-up level order traversal as:
// [
//   [15,7],
//   [9,20],
//   [3]
// ]

// 将正常的level order结果反过来就行了，Beat 91.32%

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        queue<TreeNode*> store;
        vector<vector<int>> a;
        vector<int> level;
        TreeNode* last = root;
        TreeNode* nlast = root;
        TreeNode* cur = root;
        bool index = false;
        store.push(root);

        if (!root) {
            return a;
        }

        while (cur && !store.empty()) {
            store.pop();

            if (cur->left) {
                store.push(cur->left);
                nlast = cur->left;
            }

            if (cur->right) {
                store.push(cur->right);
                nlast = cur->right;
            }

            if (cur == last) {
                level.push_back(cur->val);
                a.push_back(level);
                level.clear();
                last = nlast;
                index = true;
            }

            else {
                level.push_back(cur->val);
                index = false;
            }

            cur = store.front();

        }

        if (!index) {
            a.push_back(level);
        }

        reverse(a.begin(), a.end());    // 逆序结果

        return a;
    }
};
