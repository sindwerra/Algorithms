// 定义局部最小的概念。arr长度为1时，arr[0]是局部最小。arr的长度为N(N>1)时，
// 如果arr[0]<arr[1]，那么arr[0]是局部最小；如果arr[N-1]<arr[N-2]，
// 那么arr[N-1]是局部最小；如果0<i<N-1，既有arr[i]<arr[i-1]又有arr[i]<arr[i+1]，
// 那么arr[i]是局部最小。 给定无序数组arr，已知arr中任意两个相邻的数都不相等，
// 写一个函数，只需返回arr中任意一个局部最小出现的位置即可。

// 此题情况有长度为0，长度为1以及其他长度的情况
// 当mid值大于两端的值时，左右两边皆有符合情况的位置
// 当mid值小于两端时，mid就是一个答案
// 当mid大于左小于右时，左端就是一个碗型，必有符合情况的答案
// 当mid小于左大于右时，右端有答案
// binary search变换位点必然是end = mid - 1或者st = mid + 1这种情况

class Solution {
public:
    int getLessIndex(vector<int> arr) {
        int st = 0;
        int end = arr.size() - 1;

        if (end == 0) {
            return 0;
        }
        else if (end == -1) {
            return -1;
        }
        else if (arr[st] < arr[st + 1]) {
            return st;
        }
        else if (arr[end] < arr[end - 1]) {
            return end;
        }

        while (st <= end) {
            int mid = (st + (end - st) / 2);

            if ((arr[mid] < arr[mid + 1]) && (arr[mid] < arr[mid - 1])) {
                return mid;
            }
            else if ((arr[mid] > arr[mid - 1]) && (arr[mid] < arr[mid + 1])) {
                end = mid - 1;
            }
            else {
                st = mid + 1;
            }
        }

        return 0;
    }
};
