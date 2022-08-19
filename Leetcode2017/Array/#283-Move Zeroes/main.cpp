// 比原先版本更慢了，用的是bubble sort的思路做的

void moveZeroes(vector<int>& nums) {
            bool onemove = true;

            while(onemove) {
                onemove = false;
                for (int i = 0; i < nums.size() - 1; i++) {
                    if (nums[i] == 0 && nums[i + 1] != 0) { swap(nums[i], nums[i + 1]); onemove = true; }
                }
            }
        }
