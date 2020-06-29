/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

import "container/list"

func reversePrint(head *ListNode) []int {
	l := list.New()
	var result []int
	for head != nil {
		l.PushFront(head.Val)
		head = head.Next
	}

	for e := l.Front(); e != nil; e = e.Next() {
		result = append(result, e.Value.(int))
	}
	return result
}