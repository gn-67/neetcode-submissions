class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */

    // will the input nums be given in sorted order?

    // since each element requires a compliment in order to add up to the target
    //we could create a hashmap/object to store each number that we've seen before
    // and then while iterating through we can check if we have "seen" the compliment we need before
    //if we have, then we return the index of the "seen" value first since it must be smaller if it was seen before the current
    twoSum(nums, target) {
        let seen = {}
        for (let i = 0; i < nums.length; i++){
            let compliment = target - nums[i]
            if (compliment in seen){
                return [seen[compliment], i]
            }
            else{
                seen[nums[i]] = i
            }
        }
    }
}
