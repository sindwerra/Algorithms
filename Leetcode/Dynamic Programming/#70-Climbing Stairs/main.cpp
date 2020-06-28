class Solution {
public:
    int climbStairs(int n) {
        vector<int> result;
        result.push_back(1);
        result.push_back(1);

        for (int i = 2; i <= n; i++) {
            result.push_back(result[i - 2] + result[i - 1]);
        }

        return result[n];
    }
};
