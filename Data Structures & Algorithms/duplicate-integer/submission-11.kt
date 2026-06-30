class Solution {
    fun hasDuplicate(nums: IntArray): Boolean {
        val track: MutableSet<Int> = mutableSetOf()
        for (num in nums) {
            if (track.contains(num)) {
                return true
            } else {
                track.add(num)
            }
        }
        return false
    }
}
