
 /* Definition for a binary tree node. */
struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    void traversal(vector<int> &lst, TreeNode* root, bool direction) {
        if (root == NULL) {
            lst.push_back(-1);
            return;
        }
        lst.push_back(root->val);
        if (direction) {
            traversal(lst, root->left, direction);
            traversal(lst, root->right, direction);
        }
        else {
            traversal(lst, root->right, direction);
            traversal(lst, root->left, direction);
        }
    }

    bool isSymmetric(TreeNode* root) {
        if (root == NULL) { return true; }
        vector<int> zuo;
        vector<int> you;
        traversal(zuo, root->left, true);
        traversal(you, root->right, false);
        if (zuo.size() != you.size()) { return false; }
        for (int i = 0; i < zuo.size(); i++) {
            if (zuo[i] != you[i]) { return false; }
        }

        return true;
    }
};
