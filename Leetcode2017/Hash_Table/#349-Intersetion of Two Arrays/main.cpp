// 这题tag写的BS和Hash table，暂时没想出来对应的做法

vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        vector<int> result;
        set<int> temp;

        for (int i = 0; i < nums2.size(); i++) {
            for (int m = 0; m < nums1.size(); m++) {
                if (nums1[m] == nums2[i]) temp.insert(nums1[m]);
            }
        }

        for (set<int>::iterator it = temp.begin(); it != temp.end(); it++) {
            result.push_back(*it);
        }

        return result;
}
