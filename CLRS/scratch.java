public class Solution {
    /**
     * @param m: An integer m denotes the size of a backpack
     * @param A & V: Given n items with size A[i] and value V[i]
     * @return: The maximum value
     */
    public int backPackII(int m, int[] A, int V[]) {
        // write your code here
        int[][] ref = new int[A.length][m + 1];
        
        for (int i = 0; i < A.length; i++) {
            for (int j = 0; j < m + 1; j++) {
                ref[i][j] = 0;
            }
        }

        for (int i = 0; i < m + 1; i++) {
            if (i >= A[0]) {
                ref[0][i] = V[0];
            }
        }

        for (int i = 1; i < A.length; i++) {
            for (int j = 0; j < m + 1; j++) {
                if (j >= A[i]) {
                    ref[i][j] = Math.max(ref[i - 1][j - A[i]] + V[i], ref[i - 1][j]);
                } else {
                    ref[i][j] = ref[i - 1][j];
                }
            }
        }

        return ref[A.length][m + 1];

    }
}