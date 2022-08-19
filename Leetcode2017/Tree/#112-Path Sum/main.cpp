struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

// 递归，没什么特殊之处

bool hasPathSum(TreeNode* root, int sum) {
  bool result = false;
  HPS(root, sum, result);
  return result;
}

void HPS(TreeNode* root, int sum, bool& yes) {
  if (!root) return;
  int rem = sum - root->val;
  HPS(root->left, rem, yes);
  HPS(root->right, rem, yes);
  if (!root->left && !root->right && rem == 0) yes = true;
}
