struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

// 用last和nextlast两个指针来判断每层是否到底了，nextlast指针是随着当前node位置变化的
// 另外index这个bool变量用来让最后一层的node输入结果vector中

vector<vector<int>> levelOrder(TreeNode* root) {
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

        return a;
    }
