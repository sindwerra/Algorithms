#include <iostream>

using namespace std;

struct ListNode {
  int val;
  ListNode *next;
  ListNode(int x) : val(x), next(NULL) {}
};

void deleteNode(ListNode* node) {
  ListNode *kill = node->next;
  node->val = kill->val;
  node->next = kill->next;
  delete kill;
}
