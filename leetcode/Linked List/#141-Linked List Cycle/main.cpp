// C++ version, Beat 25.00%, First group


 // * Definition for singly-linked list.
 struct ListNode {
      int val;
      ListNode *next;
      ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode *itr = head;
        while (itr != NULL) {
            if (itr->val == 9324) { return true; }
            else {
                itr->val = 9324;
                itr = itr->next;
            }
        }
        return false;
    }
};
