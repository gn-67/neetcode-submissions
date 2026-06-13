class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */

    //how do we handle empty imputs
    
    //since each number has a corresponding compliment which adds up to the target value,
    //we can interate through the numbers and check if we have seen its coompliment before,
    //if we have we can return the index of both, with the seen index first since its guaranteed to be smaller index
    // if we haven't seen the compliment yet we can add it to an object containing the seen numbers as keys and index as valyes
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
