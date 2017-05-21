public class learning_java {
    public static class TreeNode {    // 静态类才可以被调用（为什么？)
        public int data;
        public TreeNode root;
        public TreeNode(int val, TreeNode head) {
            data = val;
            root = head;
        }

        public int getNodeVal() {
            return data;
        }
    }

    public static void main(String[] args) {
        int[] result = fib(5);
        // for (int i = 0; i < result.length; i++) {
        //     System.out.println(result[i]);
        // }

        System.out.println(Integer.parseInt("-234"));     // java字符串转整形
        TreeNode a = new TreeNode(6, null);
        System.out.println(a.getNodeVal());

        int[] b = {9, 10, 11};
        int[] x = {1, 2, 3, 4};
        System.arraycopy(b, 0, x, 2, 2);     // 一个比较有用的函数，相当于python x[3:5] = b[0:2]
        for (int j = 0; j < x.length; j++) {
            System.out.println(x[j]);
        }

        for (int k : result) {
            System.out.println(result[k]);  // 这种写法类似Python里面的 for num in results:
        }
    }

    public static int[] fib(int n) {
        int[] ref = new int[n + 1];
        ref[0] = 0;
        ref[1] = 1;
        ref[2] = 1;
        for (int i = 3; i < n + 1; i++) {
            ref[i] = ref[i - 1] + ref[i - 2];
        }

        return ref;
    }
}
