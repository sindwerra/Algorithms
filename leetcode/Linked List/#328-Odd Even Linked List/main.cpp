struct ListNode {
  int val;
  ListNode *next;
  ListNode(int x) : val(x), next(NULL) {}
};

// 速度还不错，不过代码有点多了，基本思路还是hash table定位每个node之后解链重构

ListNode* oddEvenList(ListNode* head) {
  if (head == NULL || head->next == NULL || head->next->next == NULL) {return head;}

  std::vector<ListNode*> v;
  ListNode *cur = head;
  bool jo = true;
  int count = 0;

  while (cur != NULL) {
    v.push_back(cur);
    cur = cur->next;
    v[count]->next = NULL;
    count++;
  }

  ListNode* array[v.size()];
  if (v.size() % 2 != 0) {jo = false;}

  int ji = 0;
  int ou = (v.size() - 1) / 2 + 1;  //这是index

  for (int i = 0; i < v.size(); i++) {
    if (i % 2 == 0) { array[ji++] = v[i]; }
    else { array[ou++] = v[i]; }
  }

  for (int m = 0; m < v.size() - 1; m++) {
    array[m]->next = array[m + 1];
  }

  return head;
}
