struct ListNode {
  int val;
  ListNode *next;
  ListNode(int x) : val(x), next(NULL) {}
};

// runner technique稍微改变一下，需要三个指针，链表问题一般还是有dummy node方便...
// O(n)时间复杂度，感觉没办法再快了，再快的答案应该是取巧了...

ListNode* swapPairs(ListNode* head) {
  if (head == NULL || head->next == NULL) { return head; }

  ListNode* cur = head;

  ListNode* fake = new ListNode(0);
  fake->next = head;
  head = fake;
  ListNode* prev = head;

  while (cur->next != NULL) {
    ListNode *fl = cur->next;
    cur->next = fl->next;
    fl->next = cur;
    prev->next = fl;

    cur = cur->next;
    if (cur == NULL) { break; }
    prev = fl->next;
    fl = cur->next;
  }

  return head->next;
}
