// 很简单的题，就看算法能多块了，这里有两种一种用了stack，一种是in-place的，运行速度差的很多


// in-place版本的，时间12ms

string reverseString(string s) {
    int leng = s.length();
    int index = 0;

    while (index <= leng / 2 - 1) {
        swap(s[index], s[leng - 1 - index]);
        index++;
    }

    return s;
}

// stack版本的，时间404ms

string reverseString(string s) {
        stack<char> store;
        string result = "";
        for (int i = 0; i < s.length(); i++) {
            store.push(s[i]);
        }

        while(!store.empty()) {
            result = result + store.top();
            store.pop();
        }

        return result;
    }
