#include <iostream>

using namespace std;

// 本题添加一个Dummy node解题会方便很多，一些边际情况都不用额外考虑了

struct ListNode {
  int val;
  ListNode *next;
  ListNode(int x) : val(x), next(NULL) {}
};

ListNode* removeElements(ListNode* head, int val) {
  if (head == NULL) {return NULL;}

  ListNode* fake = new ListNode(0);
  fake->next = head;
  head = fake;

  ListNode *prev = head, *cur = head->next;

  while (cur != NULL) {
    if (cur->val == val) {
      prev->next = cur->next;
      cur->next = NULL;
      cur = prev->next;
      continue;
    }

    prev = cur;
    cur = cur->next;
  }

  return head->next;
}

int main() {
  return 0;
}
