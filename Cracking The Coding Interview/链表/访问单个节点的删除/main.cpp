
struct ListNode {
    int val;
    struct ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

// 只有单节点的指针，则使用此指针的节点链接的下一个节点的值覆盖本节点的值，再删除下个节点

class Remove {
public:
    bool removeNode(ListNode* pNode) {
        // write code here
        if (pNode == nullptr) { return true; }

        if (pNode->next == nullptr) {
            delete pNode;
            return false;
        }

        pNode->val = pNode->next->val;
        ListNode* del = pNode->next;
        pNode->next = del->next;
        del->next = nullptr;
        delete del;
        return true;
    }
};
