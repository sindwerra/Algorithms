func twoSum(nums []int, target int) []int {
	result := make([]int, 2)
	dict := make(map[int]int)
	for i, v := range nums {
		if a, ok := dict[target-v]; ok {
			result[0] = a
			result[1] = i
			return result
		} else {
			dict[v] = i
		}
	}
	return result
}