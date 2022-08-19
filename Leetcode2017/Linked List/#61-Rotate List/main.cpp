struct ListNode {
  int val;
  ListNode *next;
  ListNode(int x) : val(x), next(NULL) {}
};

// 和leetcode上最初的版本不一样，边界条件很多需要考虑，不过速度最快
// 思路就是基本的链表遍历，没有用额外的数据结构

ListNode* rotateRight(ListNode* head, int k) {
  if (!head || !head->next || k == 0) { return head; }
  ListNode* cur = head;
  int size = 1;
  int count = 0;
  ListNode* now = head->next;
  ListNode* prev = head;

  while (cur->next) { size++; cur = cur->next; }

  int index = k % size;
  if (k % size == 0) {return head;}

  while (count < size - index - 1) { prev = prev->next; count++;}
  now = prev->next;
  cur->next = head;
  prev->next = NULL;
  return now;
}
