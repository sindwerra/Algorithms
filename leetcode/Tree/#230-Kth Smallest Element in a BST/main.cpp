// 中序遍历的方法，速度慢

int kthSmallest(TreeNode* root, int k) {

        vector<int> store;
        IOPrint(root, store);
        return store[k - 1];
    }

    void IOPrint(TreeNode* root, vector<int>& a) {
        if (!root) return;

        IOPrint(root->left, a);
        a.push_back(root->val);
        IOPrint(root->right, a);
    }
