class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int store = 1;
        vector<int> result;
        result.push_back(store);

        for (int i = 1; i < nums.size(); i++) {
            store *= nums[i - 1];
            result.push_back(store);
        }

        store = 1;
        for (int m = nums.size() - 2; m >= 0; m--) {
            store *= nums[m + 1];
            result[m] *= store;
        }

        return result;
    }
};
