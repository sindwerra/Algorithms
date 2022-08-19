/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func getKthFromEnd(head *ListNode, k int) *ListNode {
	dummy := head
	for i := 0; i < k; i++ {
		if dummy != nil {
			dummy = dummy.Next
		} else {
			return &ListNode{}
		}
	}

	for dummy != nil {
		head = head.Next
		dummy = dummy.Next
	}
	return head
}