
 // * Definition for singly-linked list.
 
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        if (headA == nullptr || headB == nullptr) {
            return nullptr;
        }

        ListNode *ptrA = headA;
        ListNode *ptrB = headB;

        int LA = 1;
        int LB = 1;

        while (ptrA->next != nullptr) {
            ptrA = ptrA->next;
            LA++;
        }

        while (ptrB->next != nullptr) {
            ptrB = ptrB->next;
            LB++;
        }

        if (ptrA != ptrB) {
            return nullptr;
        }

        ptrA = headA;
        ptrB = headB;
        int dist = 0;

        if (LA > LB) {
            dist = LA - LB;
            while (dist > 0) {
                ptrA = ptrA->next;
                dist--;
            }

            while ((ptrA != nullptr) && (ptrB != nullptr)) {
                if (ptrA == ptrB) {
                    return ptrA;
                }

                ptrA = ptrA->next;
                ptrB = ptrB->next;
            }
        }

        else {
            dist = LB - LA;
            while (dist > 0) {
                ptrB = ptrB->next;
                dist--;
            }

            while ((ptrA != nullptr) && (ptrB != nullptr)) {
                if (ptrA == ptrB) {
                    return ptrA;
                }

                ptrA = ptrA->next;
                ptrB = ptrB->next;
            }
        }



    }
};
