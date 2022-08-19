/*
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.


Example 1:


Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2
Example 2:


Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1

Constraints:

1 <= n <= 2000
1 <= edges.length <= 5000
edges[i].length == 2
0 <= ai <= bi < n
ai != bi
There are no repeated edges.

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/number-of-connected-components-in-an-undirected-graph
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/


// 这个解法是终极解法，但是从理解上来说有一点困难


func countComponents(n int, edges [][]int) int {
    parent := []int{}
    for i := 0; i < n; i++ {
        parent = append(parent, -1)
    }

    result := n
    for _, edge := range edges {
        a := find(parent, edge[0])
        b := find(parent, edge[1])
        if a != b {
            parent[a] = b
            result--
        }
    }
    return result
}

func find(parent []int, node int) int {
    if parent[node] == -1 {
        return node
    }
    return find(parent, parent[node])
}