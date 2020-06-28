class Solution {
public:
    int lengthOfLastWord(string s) {
    int count = 0;

    if (s.length() == 1 && s[0] == ' ') {
        return 0;
    }

    if (s[s.length() - 1] != ' ') {
        for (int i = s.length() - 1; i >= 0; i--) {
            if (s[i] == ' ') {
                break;
            }

            count++;
        }

        return count;
    }

    // substr的第二个参数是指的要取的substring的长度

    count = lengthOfLastWord(s.substr(0, s.size() - 1));

    return count;
}
};
