/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	dummy := &ListNode{}
	head := dummy
	count := 0
	for l1 != nil || l2 != nil {
		base := 0
		if l1 != nil {
			base += l1.Val
			l1 = l1.Next
		}
		if l2 != nil {
			base += l2.Val
			l2 = l2.Next
		}
		base += count
		if base > 9 {
			dummy.Next = &ListNode{Val: base - 10}
			count = 1
		} else {
			dummy.Next = &ListNode{Val: base}
			count = 0
		}
		dummy = dummy.Next
	}

	if count == 1 {
		dummy.Next = &ListNode{Val: 1}
	}
	return head.Next
}