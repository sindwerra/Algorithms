#include <iostream>

using namespace std;

struct ListNode {
  int val;
  ListNode *next;
  ListNode(int x) : val(x), next(NULL) {}
};

// 这个算法很耗时间

ListNode* deleteDuplicates(ListNode* head) {
  if (head == NULL || head->next == NULL) { return head; }

  ListNode *fake = new ListNode(0);
  fake->next = head;
  head = fake;

  ListNode *cur = head->next, *prev = head;
  // int rep = 0;

  while (cur->next != NULL) {
    if (cur->val == cur->next->val) {
      ListNode *rep = cur;
      while (rep != NULL && rep->val == cur->val) {
        rep = rep->next;
      }
      prev->next = rep;
      cur = rep;
      if (cur == NULL) { break; }
      continue;
    }

    prev = cur;
    cur = cur->next;
  }

  return head->next;
}
