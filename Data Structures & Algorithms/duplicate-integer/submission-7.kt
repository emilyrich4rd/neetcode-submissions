class Solution {
    fun hasDuplicate(nums: IntArray): Boolean {
        val setNums: Set<Int> = nums.toSet()
        return setNums.size != nums.size
    }
}
