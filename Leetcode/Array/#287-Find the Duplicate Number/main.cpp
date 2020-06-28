// 其实思路也很简单，必定有重复数且时间复杂度必须小于O(n^2)则使用快排或者归并排序再相邻
// 查找就行了，这里用的是归并排序，快排好像还有点问题，以后再来调试

void merge(vector<int>& A, int lo, int mid, int hi) {
    int i = lo - 1, j = mid, k = 0;
    int* temp = new int[hi - lo + 1];

    while (i < mid || j < hi) {
        if (i == mid) temp[k++] = A[j++];
        else if (j == hi) temp[k++] = A[i++];
        else if (A[i] < A[j]) temp[k++] = A[i++];
        else temp[k++] = A[j++];
    }

    int o = lo - 1;

    for (int m = 0; m < hi - lo + 1; m++) {
        A[o++] = temp[m];
    }
}

void mergeSort(vector<int>& A, int lo, int hi) {
    if (hi <= lo) return;

    int mid = lo + (hi - lo) / 2;

    mergeSort(A, lo, mid);
    mergeSort(A, mid + 1, hi);
    merge(A, lo, mid, hi);
}

int findDuplicate(vector<int>& nums) {
    mergeSort(nums, 1, nums.size());

    for (int i = 0; i < nums.size() - 1; i++) {
        if (nums[i] == nums[i + 1]) return nums[i];
    }

    return -1;
}
