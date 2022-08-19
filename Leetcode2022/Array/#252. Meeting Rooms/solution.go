
/*
Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: true

Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti < endi <= 106

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/meeting-rooms
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/


// 简单的扫描线原理，将数组进行排序后，只要用一个变量确保每次的meeting开始时间一定不小于该时间，那就可以都参加全


func canAttendMeetings(intervals [][]int) bool {
    if len(intervals) == 0 {
        return true
    }
    sort.Slice(intervals, func (x, y int) bool {
        return intervals[x][0] < intervals[y][0]
    })
    lastMeetingEndTime := intervals[0][1]
    for i := 1; i < len(intervals); i++ {
        if intervals[i][0] >= lastMeetingEndTime {
            lastMeetingEndTime = intervals[i][1]
        } else {
            return false
        }
    }
    return true
}

