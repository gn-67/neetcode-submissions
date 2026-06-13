class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findMin(nums) {
        let left = 0
        let right = nums.length - 1
        let curmin = nums[0]

        while (left <= right){
            if (nums[left] < nums[right]){
                curmin = Math.min(curmin, nums[left])
                return curmin
            } //this means the smallest value could be the leftmost

            let middle = Math.trunc(left + ((right - left) / 2))
            curmin = Math.min(curmin, nums[middle])

            if (nums[middle] > nums[right]){
                left = middle + 1
            }
            else{
                right = middle - 1
            }
        }

        return curmin
    }
}
