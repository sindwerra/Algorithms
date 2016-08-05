#include <iostream>
#include <vector>

using namespace std;

struct ListNode {
  int val;
  ListNode *next;
  ListNode(int x) : val(x), next(NULL) {}
};

// 这种方法用了hash table，速度很慢

ListNode* insertionSortList(ListNode* head) {
  if (head == NULL || head->next == NULL) return head;

  ListNode* fake = new ListNode(0);
  fake->next = head;
  head = fake;

  vector<ListNode*> v;
  ListNode *cur = head;
  ListNode *tra = head;

  while (cur != NULL) {
    ListNode *node = cur;
    v.push_back(node);
    cur = cur->next;
  }

  for (int i = 2; i < v.size(); i++) {
    for (int m = i; m > 1; m--) {
      if (v[m]->val < v[m - 1]->val) {
        v[m - 2]->next = v[m];
        v[m - 1]->next = v[m]->next;
        v[m]->next = v[m - 1];
        swap(v[m - 1], v[m]);
      }

      else break;
    }
    }

    return head->next;
  }
