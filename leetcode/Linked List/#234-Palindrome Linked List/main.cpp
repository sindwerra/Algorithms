// 没什么特殊用法，链表遍历先遍历一遍算出长度，然后第二遍遍历前半段数据入stack，
// 再和后半段数据对比即可


bool isPalindrome(ListNode* head) {
        stack<int> store;
        int count = 1;

        if (head == nullptr) {
            return true;
        }

        if (head->next == nullptr) {
            return true;
        }

        ListNode *cur = head;
        int length = 0;

        while (cur != nullptr) {
            cur = cur->next;
            length++;
        }

        cur = head;

        while (count <= length / 2) {
            store.push(cur->val);
            cur = cur->next;
            count++;
        }

        if (length % 2 != 0) { cur = cur->next; }

        while (cur != nullptr) {
                if (cur->val != store.top()) {
                    return false;
                }

                store.pop();
                cur = cur->next;
            }

        return true;
    }
