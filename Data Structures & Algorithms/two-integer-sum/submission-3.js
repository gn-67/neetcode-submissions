class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */

    // since we want to find the number two numbers that add up to the target we can track the number we need, or the complement, for each corresspondign 
    // create hashmap
    twoSum(nums, target) {
        let compliment = {}
        for (let i = 0; i < nums.length; i++) {
            let c = target - nums[i]
            if (c in compliment){
                return [i, compliment[c]]
            }
            else{
                compliment[nums[i]] = i
            }
        }
    }
}
