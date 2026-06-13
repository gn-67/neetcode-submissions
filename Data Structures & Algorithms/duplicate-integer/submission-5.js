class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let a = new Set(nums);
        if (a.size != nums.length) {
            return true
        }
        return false
    }

    
}
