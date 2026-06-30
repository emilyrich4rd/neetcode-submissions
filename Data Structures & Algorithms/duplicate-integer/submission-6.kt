class Solution {
    fun hasDuplicate(nums: IntArray): Boolean {
        if (nums.size < 2) {
            return false
        }
        var p1 = 0; 
        var p2 = 1;
        while (p1 != nums.size-1 || p2 != nums.size-1) {
            if (nums[p1] == nums[p2] && p1 != p2) {
                return true;
            } else {
                if (p2 == nums.size-1) {
                    p1++
                } else {
                    p2++
                }
            }
        }
        return false
    }
}
