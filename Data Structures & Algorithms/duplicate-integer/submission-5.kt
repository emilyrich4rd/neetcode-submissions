class Solution {
    fun hasDuplicate(nums: IntArray): Boolean {
        for (i in 1 until nums.size) {
            for (j in 0 until nums.size-1) {
                if (i != j && nums[i] == nums[j]) {
                    return true
                }
            }
        }
        return false
    }
}
