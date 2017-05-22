/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        if (root == null) {
            return new ArrayList<>();
        }

        List<Integer> result = new ArrayList<>();
        Stack<TreeNode> a = new Stack<>();
        Stack<TreeNode> b = new Stack<>();
        a.add(root);
        
        while (!a.empty()) {
            TreeNode node = a.pop();
            b.add(node);
            if (node.left != null) {
                a.add(node.left);
            }
            if (node.right != null) {
                a.add(node.right);
            }
        }

        while (!b.empty()) {
            result.add(b.pop().val);
        }
        return result;
    }
}