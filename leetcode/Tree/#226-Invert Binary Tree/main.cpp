struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

TreeNode* invertTree(TreeNode* root) {
  if (!root || (!root->left && !root->right)) return root;
  TreeNode* hold = NULL;
  IT(root, hold);
  return root;
}

void IT(TreeNode* root, TreeNode* hold) {
  if (!root) return;
  if (!root->left && !root->right) return;
  hold = root->right;
  root->right = root->left;
  root->left = hold;
  IT(root->left, hold);
  IT(root->right, hold);
}
