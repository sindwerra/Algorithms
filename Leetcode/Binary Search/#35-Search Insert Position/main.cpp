// 还是二分法变体，注意mid这个index要放在loop里面就行

int searchInsert(vector<int>& nums, int target) {
  int lo = 0;
  int hi = nums.size() - 1;

  if (target <= nums[0]) return 0;
  if (target > nums[hi]) return hi + 1;

  while (lo <= hi) {
    int mid = lo + (hi - lo) / 2;
    if (target == nums[mid]) return mid;
    if (target > nums[mid] && target <= nums[mid + 1]) return mid + 1;
    if (target < nums[mid]) hi = mid - 1;
    else if (target > nums[mid + 1]) lo = mid + 1;
  }

  return -1;
}
