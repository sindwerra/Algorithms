"
判教题... 借鉴的还是LCsubtring的思路，把这个string反过来找公共最长子序列就是它的最长对称子序列了
虽说算是取巧了，但毕竟还是保持了DP的思路，算不上作弊，另外java跟Python的时间性能真的差的太明显了...
Beat 23.73%
公司：Amazon, Uber
"

public class Solution {
    public int longestPalindromeSubseq(String s) {
        String k = new StringBuilder(s).reverse().toString();
        return LCS(s, k, k.length());
    }

    public int LCS(String A, String B, int n) {
        int[][] ref = new int[n + 1][n + 1];
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= n; j++) {
                ref[i][j] = 0;
            }
        }

        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j < n + 1; j++) {
                if (A.charAt(i - 1) == B.charAt(j - 1)) {
                    ref[i][j] = ref[i - 1][j - 1] + 1;
                } else {
                    ref[i][j] = Math.max(ref[i - 1][j], ref[i][j - 1]);
                }
            }
        }

        return ref[n][n];
    }
}