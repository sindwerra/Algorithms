// 辅助函数加引用输入变量和递归法是完美搭档

vector<vector<int>> pathSum(TreeNode* root, int sum) {
  vector<int> temp;
  vector<vector<int>> result;
  PSII(root, temp, result, sum);
  return result;
}

void PSII(TreeNode* root, vector<int>& temp, vector<vector<int>>& result, int sum) {
  if (!root) return;
  temp.push_back(root->val);
  int rem = sum - root->val;
  PSII(root->left, temp, result, rem);
  PSII(root->right, temp, result, rem);
  if (!root->left && !root->right && rem == 0) result.push_back(temp);
  temp.erase(temp.end() - 1);
}
