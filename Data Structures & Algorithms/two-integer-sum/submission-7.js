class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */

    //since each number wihtin nums requires a compliment to add up to the target
    //we can create an object to track the values that we've seen and their indices, and then check if the compliment of the current value exists in our seen values
    //if it does we rreturn it with the current value, else we keep searching and add the current value to our seen list
    twoSum(nums, target) {
        let seen = {}
        for (let i = 0; i < nums.length; i++){
            let compliment = target - nums[i]
            if (compliment in seen){
                return [seen[compliment], i]
            }
            if (nums[i] in seen){
                continue
            }
            else{
                seen[nums[i]] = i
            }
        }
    }
}
